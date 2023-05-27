import os
import shutil
import datetime


class StockDataBackup:
    def __init__(self, data_dir, backup_dir, retention_days):
        self.data_dir = data_dir
        self.backup_dir = backup_dir
        self.retention_days = retention_days

    def create_backup(self):
        # Create a backup directory with the current timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(self.backup_dir, timestamp)
        os.makedirs(backup_path, exist_ok=True)

        # Copy all files from the data directory to the backup directory
        for root, dirs, files in os.walk(self.data_dir):
            for file in files:
                src_path = os.path.join(root, file)
                dst_path = os.path.join(backup_path, os.path.relpath(src_path, self.data_dir))
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                shutil.copy(src_path, dst_path)

    def cleanup_backups(self):
        # Get the cutoff date for backups
        cutoff_date = datetime.datetime.now() - datetime.timedelta(days=self.retention_days)

        # Iterate over the backup directories
        for entry in os.scandir(self.backup_dir):
            if entry.is_dir():
                try:
                    # Get the timestamp from the backup directory name
                    timestamp = datetime.datetime.strptime(entry.name, "%Y%m%d_%H%M%S")

                    # Remove the backup directory if it's older than the cutoff date
                    if timestamp < cutoff_date:
                        shutil.rmtree(entry.path)
                except ValueError:
                    # Skip directories with invalid names
                    continue