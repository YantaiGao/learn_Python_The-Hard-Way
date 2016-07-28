try
	from setuptools import setup
except ImportError
	from distutils.core import setup
	
config = [
	"description":"ex47 project for test",
	"author":"gyt",
	"url":"url to get it at.",
	"download_url":"where to download it",
	"author_mail":"gaoyantai@gmail.com",
	"version":"0.1",
	"install_requires":['nose'],
	"packages":['Model'],
	"scripts":[],
	"name":"project_ex47"	
]
	
setup(**config)