# Django Todo

This project contains a demo of integrating flowbite UI components and tailwind CSS with django jinja templaptes.


Requirements
- Python
- NodeJS

### To make changes to the project

- Clone the project

```shell
git clone https://github.com/jveer634/django-flowbite-demo.git
cd django-flowbite-demo
pip install -r requirements.txt
```
- After installing the dependencies, run the below command to start the tailwind CSS
```shell
python manage.py tailwind start
```

- Now open another terminal to start the django server
```shell
  python manage.py runserver
```


To tun the project on a linux / mac machine, the change the `NPM_BIN_PATH` in the `settings.py` file to your Node Js location.

https://github.com/jveer634/django-flowbite-demo/blob/1fdf90fd91847b703cd53100c605abbee0257965/core/settings.py#L141
