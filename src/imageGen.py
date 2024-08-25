from jinja2 import Template
from pathlib import Path


class ImageGen:

    def __init__(
        self, template_filename: str, output_filename: str, template_data: dict
    ) -> None:
        self.template_path = Path(__file__).parent / template_filename
        self.file_name = output_filename
        self.data = template_data
        self.add_template()
        self.gen_str()
        self.gen_file()

    def add_template(self):
        with open(self.template_path, mode="r", encoding="utf-8") as template_file:
            template_content = template_file.read()
        # Create a Jinja2 template
        self.template = Template(template_content)

    def gen_str(self):
        self.doc = self.template.render(self.data)

    def gen_file(self):
        with open(self.file_name, "w+", encoding="utf-8") as f:
            f.write(self.doc)


if __name__ == "__main__":
    template_data1 = {"hero_title": "readme-generator"}
    ImageGen("hero_template.svg", "../docs/assets/images/hero.svg", template_data1)
    template_data2 = {
        "badge_title": "GMAIL",
        "left_color": "#314042",
        "right_color": "#263759",
        "img_color": "#fff",
        "badge_img": "data:image/svg+xml;base64,PHN2ZyBmaWxsPSJ3aGl0ZSIgcm9sZT0iaW1nIiB2aWV3Qm94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHRpdGxlPkdtYWlsPC90aXRsZT48cGF0aCBkPSJNMjQgNS40NTd2MTMuOTA5YzAgLjkwNC0uNzMyIDEuNjM2LTEuNjM2IDEuNjM2aC0zLjgxOVYxMS43M0wxMiAxNi42NGwtNi41NDUtNC45MXY5LjI3M0gxLjYzNkExLjYzNiAxLjYzNiAwIDAgMSAwIDE5LjM2NlY1LjQ1N2MwLTIuMDIzIDIuMzA5LTMuMTc4IDMuOTI3LTEuOTY0TDUuNDU1IDQuNjQgMTIgOS41NDhsNi41NDUtNC45MSAxLjUyOC0xLjE0NUMyMS42OSAyLjI4IDI0IDMuNDM0IDI0IDUuNDU3eiIvPjwvc3ZnPg==",
        "text_color": "#fff",
        "badge_text": "ReadmeGenerator",
    }
    ImageGen("badge_template.svg", "../docs/assets/images/badge.svg", template_data2)
    template_data3 = {
        "badge_title": "License",
        "left_color": "#314042",
        "right_color": "#263759",
        "left_text": "License",
        "right_text": "GPL-3.0",
    }
    ImageGen("textbadge_template.svg", "textbadge.svg", template_data3)
    template_data4 = {"label": "License", "label_color": "#314042"}
    ImageGen("label_template.svg", "../docs/assets/images/label.svg", template_data4)
