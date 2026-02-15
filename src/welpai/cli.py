import click
from .core import WelpAi

@click.group()
def main():
    pass

@main.command()
@click.argument('model_name')
def set(model_name):
    ai = WelpAi()
    real_name = ai.save_model(model_name)
    click.secho(f"✅ Настройки WelpAi обновлены!", fg="cyan")
    click.echo(f"Текущая модель: {real_name}")

@main.command()
@click.argument('prompt')
def ask(prompt):
    ai = WelpAi()
    model = ai.get_saved_model()
    click.secho(f"⚡ [WelpAi Engine: {model}] Генерирую ответ...", fg="yellow", nl=False)
    result = ai.chat(prompt)
    click.echo("\r" + " " * 60 + "\r", nl=False)
    click.secho(result, fg="green")

@main.command()
def models():
    click.secho("🌌 Доступные архитектуры WelpAi:", fg="magenta", bold=True)
    click.echo(" - gpt-oss (Флагманская 120B)")
    click.echo(" - llama-70b (Универсальная)")
    click.echo(" - qwen (Мощная)")
    click.echo(" - llama-8b (Быстрая)")
    click.echo(" - zai-glm (Экспериментальная)")
