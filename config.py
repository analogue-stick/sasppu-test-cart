import sys, os
if sys.implementation.name == "micropython":
    apps = os.listdir("/apps")
    path = ""
    for app in apps:
        if app.startswith("sasppu-test-cart"):
            path = "/apps/" + app
    ASSET_PATH = path + "/assets/"
else:
    ASSET_PATH = "./apps/sasppu-test-cart/assets/"