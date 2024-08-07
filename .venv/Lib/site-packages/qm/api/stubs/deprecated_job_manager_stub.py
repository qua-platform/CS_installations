from typing import TYPE_CHECKING, Optional

import betterproto

from qm.grpc.job_manager import InsertInputStreamResponse, GetElementCorrectionResponse, SetElementCorrectionResponse

if TYPE_CHECKING:
    from qm.grpc.job_manager import (
        Deadline,
        MetadataLike,
        InsertInputStreamRequest,
        GetElementCorrectionRequest,
        SetElementCorrectionRequest,
    )


class DeprecatedJobManagerServiceStub(betterproto.ServiceStub):
    async def get_element_correction(
        self,
        get_element_correction_request: "GetElementCorrectionRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "GetElementCorrectionResponse":
        return await self._unary_unary(
            "/qm.grpc.jobManager.JobManagerService/GetElementCorrection",
            get_element_correction_request,
            GetElementCorrectionResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def set_element_correction(
        self,
        set_element_correction_request: "SetElementCorrectionRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "SetElementCorrectionResponse":
        return await self._unary_unary(
            "/qm.grpc.jobManager.JobManagerService/SetElementCorrection",
            set_element_correction_request,
            SetElementCorrectionResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def insert_input_stream(
        self,
        insert_input_stream_request: "InsertInputStreamRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None,
    ) -> "InsertInputStreamResponse":
        return await self._unary_unary(
            "/qm.grpc.jobManager.JobManagerService/InsertInputStream",
            insert_input_stream_request,
            InsertInputStreamResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )
