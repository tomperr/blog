def path_and_rename(instance, filename):
    upload_to = 'speedpost/images'
    ext = filename.split('.')[-1]
    nb = len(SpeedPost.objects.all())+1
    filename = "{}.{}".format(nb, ext)
    return os.path.join(upload_to, filename)