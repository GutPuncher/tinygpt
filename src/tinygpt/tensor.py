from __future__ import annotations
from typing import Any

from tinygpt.utils import DType
from tinygpt.buffer import Buffer


class Tensor():

    def __init__(
            self,
            data: Any,
            dtype: DType = None,
            requires_grad=False
    ) -> None:
        # Save the data in a buffer
        self.buffer = Buffer(data, dtype)

        # Gradient-related metadata
        self.requires_grad = requires_grad
        self.grad = None
        self.grad_fn = None

        # Only float tensors can require gradients
        if self.requires_grad and self.dtype != DType.float32:
            raise RuntimeError("Only Tensors of floating point dtype can require gradients")

    def __repr__(self) -> str:
        return f"<Tensor {self.buffer}, shape={self.shape}, dtype={self.dtype}, requires_grad={self.requires_grad}>"

    @property
    def shape(self):
        return self.buffer.shape

    @property
    def ndim(self):
        return self.buffer.ndim

    @property
    def dtype(self):
        return self.buffer.dtype
