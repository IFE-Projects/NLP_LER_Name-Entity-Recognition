import spacy_streamlit
import typer
import os


def main(models_dir: str, default_text: str):
    models = [f'./{models_dir}/{model_dir}/model-best' for model_dir in os.listdir(models_dir)]
    #models = [name.strip() for name in models.split(",")]
    spacy_streamlit.visualize(models, default_text, visualizers=["ner"])


if __name__ == "__main__":
    try:
        typer.run(main)
    except SystemExit:
        pass
