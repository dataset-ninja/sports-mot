Dataset **SportsMOT** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/x/w/mt/jVKOQ23jM0kRJ7fKuctrtQyrq0gaPPZcx1T8YQd4zk8rolbK4Qs4wEyHCjF0NPHExE7igi3Y05YbPqTdvzniIPCukUuREKzhdcIk3AkwQmyQ7KrOKsJ9tlRVl02Y.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='SportsMOT', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://1drv.ms/u/s!AtjeLq7YnYGRgQPmuAkwWhndOc41?e=ItJaaa).