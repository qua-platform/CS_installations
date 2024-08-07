from typing import List, Generic, TypeVar

T = TypeVar("T")


class Chunk(Generic[T]):
    def __init__(self) -> None:
        self._data: List[T] = []
        self._accepts_different = True

    def add(self, element: T) -> None:
        if self._data and element == self._data[-1]:
            self._data.append(element)
            self._accepts_different = False
            return

        if self.accepts_different:
            self._data.append(element)
            return

        raise ValueError("Tried to add number to a chunk that is already uniform")

    def __len__(self) -> int:
        return len(self._data)

    @property
    def data(self) -> List[T]:
        return self._data

    @property
    def first(self) -> T:
        return self._data[0]

    @property
    def accepts_different(self) -> bool:
        return self._accepts_different

    def __str__(self) -> str:
        if self.accepts_different:
            return str(self._data)
        return f"[{self.first}] * {len(self)}"


def split_list_to_chunks(list_data: List[T]) -> List[Chunk[T]]:
    curr_chunk: Chunk[T] = Chunk()
    chunks = [curr_chunk]
    for idx, curr_item in enumerate(list_data):
        if idx >= 1 and curr_item != list_data[idx - 1]:
            item_equals_next = idx < len(list_data) - 1 and curr_item == list_data[idx + 1]
            if item_equals_next or not curr_chunk.accepts_different:
                curr_chunk = Chunk()
                chunks.append(curr_chunk)

        curr_chunk.add(curr_item)
    return chunks
