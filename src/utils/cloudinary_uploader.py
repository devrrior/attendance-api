import uuid

import cloudinary
from cloudinary.uploader import upload

from src.config import settings


class CloudinaryUploader:
    @staticmethod
    def upload_file(filename, folder="/attendance-reports"):
        cloudinary.config(
            cloud_name=settings.CLOUDINARY_CLOUD_NAME,
            api_key=settings.CLOUDINARY_API_KEY,
            api_secret=settings.CLOUDINARY_API_SECRET
        )
        report_id = str(uuid.uuid4())

        upload_result = upload(filename, folder=folder, filename_override=f"$report-{report_id}.xlsx",
                               resource_type="raw")

        return upload_result["url"]
