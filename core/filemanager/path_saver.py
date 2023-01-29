def user_image_upload_to(instance, file):
    ext = file.split(".")[-1]
    return f"users/{instance.id}/image.{ext}"


