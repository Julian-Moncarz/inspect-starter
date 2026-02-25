from inspect_ai import Task, task
from inspect_ai.dataset import Sample
from inspect_ai.scorer import model_graded_fact
from inspect_ai.solver import generate

@task
def hello_inspect():
    """A minimal Inspect task to verify your setup works."""
    return Task(
        dataset=[
            Sample(
                input="What is the capital of France?",
                target="Paris",
            )
        ],
        solver=generate(),
        scorer=model_graded_fact(),
    )
