from pathlib import Path

class Dataset:
    def __init__(self, dataset_path):
        self.dataset_path = Path(dataset_path)
        
        if not self.dataset_path.exists() or not self.dataset_path.is_dir():
            raise Exception("Dataset path does not exist or is not a directory")

        self._load_dataset()

    def _load_tags(file_name):
        file_path = Path(file_name).with_suffix(".txt")

        if not file_path.exists() or not file_path.is_file():
            return None

        return [tag.strip() for tag in file_path.read_text().split(",")]

    def _load_dataset(self):
        self.dataset = {
            file_name: Dataset._load_tags(file_name) for file_name in self.dataset_path.iterdir() if file_name.is_file() and file_name.suffix in [".png", ".jpg", ".jpeg", ".webp"]
        }