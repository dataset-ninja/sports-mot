import os
import shutil
from collections import defaultdict

import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import (
    file_exists,
    get_file_name,
    get_file_name_with_ext,
    get_file_size,
)
from tqdm import tqdm

import src.settings as s


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # Possible structure for bbox case. Feel free to modify as you needs.

    all_images_path = "/home/alex/DATASETS/TODO/sportsmot_publish/dataset"
    split_path = "/home/alex/DATASETS/TODO/sportsmot_publish/splits_txt"
    batch_size = 30

    def create_ann(image_path):
        labels = []

        # image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = 720  # image_np.shape[0]
        img_wight = 1280  # image_np.shape[1]

        if ds_name == "test":
            return sly.Annotation(
                img_size=(img_height, img_wight), labels=labels, img_tags=[seq, sport]
            )

        ann_data = im_name_to_data[get_file_name_with_ext(image_path)]
        for curr_ann_data in ann_data:
            tag = sly.Tag(identity_meta, value=int(curr_ann_data[0]))

            left = int(curr_ann_data[1])
            top = int(curr_ann_data[2])
            right = left + int(curr_ann_data[3])
            bottom = top + int(curr_ann_data[4])

            rect = sly.Rectangle(left=left, top=top, right=right, bottom=bottom)
            label = sly.Label(rect, obj_class, tags=[tag])
            labels.append(label)

        return sly.Annotation(
            img_size=(img_height, img_wight), labels=labels, img_tags=[seq, sport]
        )

    obj_class = sly.ObjClass("person", sly.Rectangle)

    identity_meta = sly.TagMeta("person id", sly.TagValueType.ANY_NUMBER)
    seq_meta = sly.TagMeta("sequence", sly.TagValueType.ANY_STRING)
    basketball_meta = sly.TagMeta("basketball", sly.TagValueType.NONE)
    football_meta = sly.TagMeta("football", sly.TagValueType.NONE)
    volleyball_meta = sly.TagMeta("volleyball", sly.TagValueType.NONE)

    with open(os.path.join(split_path, "basketball.txt")) as f:
        basketball_seq = f.read().split("\n")

    with open(os.path.join(split_path, "football.txt")) as f:
        football_seq = f.read().split("\n")

    with open(os.path.join(split_path, "volleyball.txt")) as f:
        volleyball_seq = f.read().split("\n")

    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(
        obj_classes=[obj_class],
        tag_metas=[identity_meta, seq_meta, basketball_meta, football_meta, volleyball_meta],
    )
    api.project.update_meta(project.id, meta.to_json())

    for ds_name in os.listdir(all_images_path):

        dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

        curr_data_path = os.path.join(all_images_path, ds_name)

        for subfolder in os.listdir(curr_data_path):

            seq = sly.Tag(seq_meta, value=subfolder)
            if subfolder in basketball_seq:
                sport = sly.Tag(basketball_meta)
            elif subfolder in football_seq:
                sport = sly.Tag(football_meta)
            elif subfolder in volleyball_seq:
                sport = sly.Tag(volleyball_meta)

            images_path = os.path.join(curr_data_path, subfolder, "img1")
            ann_path = os.path.join(curr_data_path, subfolder, "gt", "gt.txt")

            if ds_name != "test":
                im_name_to_data = defaultdict(list)
                with open(ann_path) as f:
                    content = f.read().split("\n")
                    for row in content:
                        if len(row) > 0:
                            row_data = row.split(", ")
                            im_name_to_data[row_data[0].zfill(6) + ".jpg"].append(row_data[1:])

            images_names = os.listdir(images_path)

            progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

            for images_names_batch in sly.batched(images_names, batch_size=batch_size):
                im_names_batch = []
                img_pathes_batch = []
                for image_name in images_names_batch:
                    img_pathes_batch.append(os.path.join(images_path, image_name))
                    im_names_batch.append(subfolder + "_" + image_name)

                img_infos = api.image.upload_paths(dataset.id, im_names_batch, img_pathes_batch)
                img_ids = [im_info.id for im_info in img_infos]

                anns = [create_ann(image_path) for image_path in img_pathes_batch]
                api.annotation.upload_anns(img_ids, anns)

                progress.iters_done_report(len(images_names_batch))

    return project
