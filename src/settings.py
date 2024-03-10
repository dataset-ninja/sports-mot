from typing import Dict, List, Literal, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "SportsMOT"
PROJECT_NAME_FULL: str = "SportsMOT Dataset"
HIDE_DATASET = True  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC_BY_NC_4_0(source_url="https://github.com/MCG-NJU/SportsMOT#Terms")
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Sports()]
CATEGORY: Category = Category.Sports()

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.ObjectDetection()]

RELEASE_DATE: Optional[str] = "2023-04-13"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://deeperaction.github.io/datasets/sportsmot.html"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 15159310
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/sports-mot"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = (
    "https://1drv.ms/u/s!AtjeLq7YnYGRgQPmuAkwWhndOc41?e=ItJaaa"
)
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]] or Literal["predefined"]] = "predefined"
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
# Use dict key to specify name for a button
PAPER: Optional[Union[str, List[str], Dict[str, str]]] = "https://arxiv.org/pdf/2304.05170v2"
BLOGPOST: Optional[Union[str, List[str], Dict[str, str]]] = None
REPOSITORY: Optional[Union[str, List[str], Dict[str, str]]] = {
    "GitHub": "https://github.com/MCG-NJU/SportsMOT",
    "CodaLab": "https://codalab.lisn.upsaclay.fr/competitions/12424",
}

CITATION_URL: Optional[str] = None
AUTHORS: Optional[List[str]] = [
    "Yutao Cui",
    "Chenkai Zeng",
    "Xiaoyu Zhao",
    "Yichun Yang",
    "Gangshan Wu",
    "Limin Wang",
]
AUTHORS_CONTACTS: Optional[List[str]] = ["lmwang.nju@gmail.com"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "Nanjing University, China"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://mcg.nju.edu.cn/"

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with string value to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = {
    "kinds of sports": ["basketball", "football", "volleyball"],
    "__POSTTEXT__": "Additionally, every image marked with its ***sequence*** tag. Every label contains information about its ***person id***. Explore it in Supervisely labelling tool",
}
TAGS: Optional[
    List[Literal["multi-view", "synthetic", "simulation", "multi-camera", "multi-modal"]]
] = None


SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["repository"] = REPOSITORY
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
