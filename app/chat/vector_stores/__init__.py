from functools import partial
from .chrodb import build_retriever

retriever_map = {
    "chrodb_1": partial(build_retriever, k=1),
    "chrodb_2": partial(build_retriever, k=2),
    "chrodb_3": partial(build_retriever, k=3)
}