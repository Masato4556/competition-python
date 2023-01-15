import shutil
import datetime

dt_now = datetime.datetime.now()
dir_name  = "./{}".format(dt_now.strftime('%Y%m%d%H%M%S'))
shutil.copytree("./template", dir_name)