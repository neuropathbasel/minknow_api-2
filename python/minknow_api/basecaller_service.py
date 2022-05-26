### THIS FILE IS AUTOGENERATED. DO NOT EDIT THIS FILE DIRECTLY ###
import minknow_api
from minknow_api.basecaller_pb2_grpc import *
import minknow_api.basecaller_pb2 as basecaller_pb2
from minknow_api.basecaller_pb2 import *
from minknow_api._support import MessageWrapper, ArgumentError
import time
import logging
import sys

__all__ = [
    "Basecaller",
    "ListConfigsByKitRequest",
    "ListConfigsByKitResponse",
    "StartBasecallingRequest",
    "StartBasecallingResponse",
    "StartBarcodingRequest",
    "StartBarcodingResponse",
    "StartAlignmentRequest",
    "StartAlignmentResponse",
    "StartPostProcessingProtocolRequest",
    "StartRequest",
    "StartPostProcessingProtocolResponse",
    "CancelRequest",
    "CancelResponse",
    "RunInfo",
    "GetInfoRequest",
    "GetInfoResponse",
    "WatchRequest",
    "WatchResponse",
    "MakeAlignmentIndexRequest",
    "MakeAlignmentIndexResponse",
    "ListPostProcessingProtocolsRequest",
    "PostProcessingProtocolInfo",
    "ListPostProcessingProtocolsResponse",
    "ListSettingsForPostProcessingProtocolRequest",
    "ListSettingsForPostProcessingProtocolResponse",
    "UpdateProgressRequest",
    "UpdateProgressResponse",
    "SendPingRequest",
    "SendPingResponse",
    "State",
    "STATE_RUNNING",
    "STATE_SUCCESS",
    "STATE_ERROR",
    "STATE_CANCELLED",
    "SelectionPreset",
    "PRESET_ALL_RUNNING",
    "PRESET_MOST_RECENTLY_STARTED",
    "PRESET_ALL",
    "PostProcessingProvider",
    "SCRIPT",
    "EPI2ME",
]

def run_with_retry(method, message, timeout, unwraps, full_name):
    retry_count = 20
    error = None
    for i in range(retry_count):
        try:
            result = MessageWrapper(method(message, timeout=timeout), unwraps=unwraps)
            return result
        except grpc.RpcError as e:
            # Retrying unidentified grpc errors to keep clients from crashing
            retryable_error = (e.code() == grpc.StatusCode.UNKNOWN and "Stream removed" in e.details() or \
                                (e.code() == grpc.StatusCode.INTERNAL and "RST_STREAM" in e.details()))
            if retryable_error:
                logging.info('Bypassed ({}: {}) error for grpc: {}. Attempt {}.'.format(e.code(), e.details(), full_name, i))
            else:
                raise
            error = e
        time.sleep(1)
    raise error


class Basecaller(object):
    """Basecall reads files from previous sequencing runs.

    NB: this is not available from a MinKNOW device instance. It should be accessed on its own
    connection, using one of the ports provided by the
    minknow_api.manager.ManagerService.basecaller_api() method.

    Since 3.5"""
    def __init__(self, channel):
        self._stub = BasecallerStub(channel)
        self._pb = basecaller_pb2
    def list_configs_by_kit(self, _message=None, _timeout=None, **kwargs):
        """List the available basecalling configurations sorted by flow cell and kit.

        Since 3.5

        This RPC has no side effects. Calling it will have no effect on the state of the
        system. It is safe to call repeatedly, or to retry on failure, although there is no
        guarantee it will return the same information each time.

        Args:
            _message (minknow_api.basecaller_pb2.ListConfigsByKitRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.

        Returns:
            minknow_api.basecaller_pb2.ListConfigsByKitResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.list_configs_by_kit,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.basecaller.Basecaller")

        unused_args = set(kwargs.keys())

        _message = ListConfigsByKitRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to list_configs_by_kit: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.list_configs_by_kit,
                              _message, _timeout,
                              [],
                              "minknow_api.basecaller.Basecaller")
    def start_basecalling(self, _message=None, _timeout=None, **kwargs):
        """Start basecalling reads files.

        Since 4.0

        

        Args:
            _message (minknow_api.basecaller_pb2.StartBasecallingRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            name (str, optional): User specified name to identify the basecall run.
            input_reads_directories (str, optional): Input directories to search for reads to be basecalled.

                Currently, only one directory can be specified, but this definition allows for multiple in
                the future without breaking compatibility.
            output_reads_directory (str, optional): Output directory where called reads will be placed.

                Reads will be sorted into subdirectories based on the sequencing run they came from.
            configuration (str, optional): The name of the basecalling configuration to use.
            fast5_out (bool, optional): Enable output of .fast5 files containing original raw reads, event data/trace table from
                basecall and basecall result sequence.

                This causes .fast5 files to be output in addition to FASTQ files.
            compress_fastq (bool, optional): Enable gzip compression of output FASTQ files.
            disable_events (bool, optional): Prevent events / trace tables being written to .fast5 files.

                If event tables are not required for downstream processing (eg: for 1d^2) then it is more
                efficient (and produces smaller files) to disable them.

                This has no effect if ``fast5_out`` is not enabled.
            recursive (bool, optional): Recursively find fast5 files to basecall in the `input_reads_directories`.

                If False, only the fast5 files directly in one of the `input_reads_directories` will be
                basecalled. If True, subdirectories of those directories will also be searched recursively.
            barcoding_configuration (minknow_api.analysis_configuration_pb2.BarcodingConfiguration, optional): Options to control barcoding performed once basecalling reads is complete.
            alignment_configuration (minknow_api.analysis_configuration_pb2.AlignmentConfiguration, optional): Options to control alignment performed once basecalling reads is complete.

        Returns:
            minknow_api.basecaller_pb2.StartBasecallingResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.start_basecalling,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.basecaller.Basecaller")

        unused_args = set(kwargs.keys())

        _message = StartBasecallingRequest()

        if "name" in kwargs:
            unused_args.remove("name")
            _message.name = kwargs['name']

        if "input_reads_directories" in kwargs:
            unused_args.remove("input_reads_directories")
            _message.input_reads_directories.extend(kwargs['input_reads_directories'])

        if "output_reads_directory" in kwargs:
            unused_args.remove("output_reads_directory")
            _message.output_reads_directory = kwargs['output_reads_directory']

        if "configuration" in kwargs:
            unused_args.remove("configuration")
            _message.configuration = kwargs['configuration']

        if "fast5_out" in kwargs:
            unused_args.remove("fast5_out")
            _message.fast5_out = kwargs['fast5_out']

        if "compress_fastq" in kwargs:
            unused_args.remove("compress_fastq")
            _message.compress_fastq = kwargs['compress_fastq']

        if "disable_events" in kwargs:
            unused_args.remove("disable_events")
            _message.disable_events = kwargs['disable_events']

        if "recursive" in kwargs:
            unused_args.remove("recursive")
            _message.recursive = kwargs['recursive']

        if "barcoding_configuration" in kwargs:
            unused_args.remove("barcoding_configuration")
            _message.barcoding_configuration.CopyFrom(kwargs['barcoding_configuration'])

        if "alignment_configuration" in kwargs:
            unused_args.remove("alignment_configuration")
            _message.alignment_configuration.CopyFrom(kwargs['alignment_configuration'])

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to start_basecalling: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.start_basecalling,
                              _message, _timeout,
                              [],
                              "minknow_api.basecaller.Basecaller")
    def start_barcoding(self, _message=None, _timeout=None, **kwargs):
        """Start barcoding fastq files.

        Since 3.8

        

        Args:
            _message (minknow_api.basecaller_pb2.StartBarcodingRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            name (str, optional): User specified name to identify the barcoding run.
            input_reads_directories (str, optional): Input directories to search for reads to be basecalled.

                Currently, only one directory can be specified, but this definition allows for multiple in
                the future without breaking compatibility.
            output_reads_directory (str, optional): Output directory where called reads will be placed.

                Reads will be sorted into subdirectories based on the sequencing run they came from.
            compress_fastq (bool, optional): Enable gzip compression of output FASTQ files.
            recursive (bool, optional): Recursively find fast5 files to basecall in the `input_reads_directories`.

                If False, only the fast5 files directly in one of the `input_reads_directories` will be
                basecalled. If True, subdirectories of those directories will also be searched recursively.
            barcoding_configuration (minknow_api.analysis_configuration_pb2.BarcodingConfiguration, optional): Options to control barcoding performed once basecalling reads is complete.

        Returns:
            minknow_api.basecaller_pb2.StartBarcodingResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.start_barcoding,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.basecaller.Basecaller")

        unused_args = set(kwargs.keys())

        _message = StartBarcodingRequest()

        if "name" in kwargs:
            unused_args.remove("name")
            _message.name = kwargs['name']

        if "input_reads_directories" in kwargs:
            unused_args.remove("input_reads_directories")
            _message.input_reads_directories.extend(kwargs['input_reads_directories'])

        if "output_reads_directory" in kwargs:
            unused_args.remove("output_reads_directory")
            _message.output_reads_directory = kwargs['output_reads_directory']

        if "compress_fastq" in kwargs:
            unused_args.remove("compress_fastq")
            _message.compress_fastq = kwargs['compress_fastq']

        if "recursive" in kwargs:
            unused_args.remove("recursive")
            _message.recursive = kwargs['recursive']

        if "barcoding_configuration" in kwargs:
            unused_args.remove("barcoding_configuration")
            _message.barcoding_configuration.CopyFrom(kwargs['barcoding_configuration'])

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to start_barcoding: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.start_barcoding,
                              _message, _timeout,
                              [],
                              "minknow_api.basecaller.Basecaller")
    def start_post_processing_protocol(self, _message=None, _timeout=None, **kwargs):
        """Start an post processing analysis protocol.

        Post processing protocols allow processing already generated sequencing files in some way, eg: running an
        ARTIC workflow on some fastq files, or barcoding a set of fastq input files.

        Since 4.4

        

        Args:
            _message (minknow_api.basecaller_pb2.StartPostProcessingProtocolRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            identifier (str, optional): identifier value from a protocol returned from list_post_processing_protocols.
            sequencing_protocol_run_id (str, optional): Optionally specify a sequencing protocol that is linked with this analysis.
            input_fast5_directory (str, optional): Input directories for the protocol (omit those which the protocol doesn't require).
            input_fastq_directory (str, optional): 
            input_bam_directory (str, optional): 
            sample_sheet_path (str, optional): Path to the sample sheet output by minknow
            output_directory (str, optional): Output directory where the analysed output should be written.
            setting_values (minknow_api.basecaller_pb2.StartPostProcessingProtocolRequest.SettingValuesEntry, optional): Configured values for display settings for the protocol (see basecaller.list_settings_for_protocol)
                keys missing from the original protocol will cause errors.

        Returns:
            minknow_api.basecaller_pb2.StartPostProcessingProtocolResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.start_post_processing_protocol,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.basecaller.Basecaller")

        unused_args = set(kwargs.keys())

        _message = StartPostProcessingProtocolRequest()

        if "identifier" in kwargs:
            unused_args.remove("identifier")
            _message.identifier = kwargs['identifier']

        if "sequencing_protocol_run_id" in kwargs:
            unused_args.remove("sequencing_protocol_run_id")
            _message.sequencing_protocol_run_id = kwargs['sequencing_protocol_run_id']

        if "input_fast5_directory" in kwargs:
            unused_args.remove("input_fast5_directory")
            _message.input_fast5_directory = kwargs['input_fast5_directory']

        if "input_fastq_directory" in kwargs:
            unused_args.remove("input_fastq_directory")
            _message.input_fastq_directory = kwargs['input_fastq_directory']

        if "input_bam_directory" in kwargs:
            unused_args.remove("input_bam_directory")
            _message.input_bam_directory = kwargs['input_bam_directory']

        if "sample_sheet_path" in kwargs:
            unused_args.remove("sample_sheet_path")
            _message.sample_sheet_path = kwargs['sample_sheet_path']

        if "output_directory" in kwargs:
            unused_args.remove("output_directory")
            _message.output_directory = kwargs['output_directory']

        if "setting_values" in kwargs:
            unused_args.remove("setting_values")
            for key, value in kwargs['setting_values'].items():
                _message.setting_values[key].CopyFrom(value)

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to start_post_processing_protocol: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.start_post_processing_protocol,
                              _message, _timeout,
                              [],
                              "minknow_api.basecaller.Basecaller")
    def start_alignment(self, _message=None, _timeout=None, **kwargs):
        """Start aligning fastq files.

        Since 3.8

        

        Args:
            _message (minknow_api.basecaller_pb2.StartAlignmentRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            name (str, optional): User specified name to identify the alignment run.
            input_reads_directories (str, optional): Input directories to search for reads to be aligned.

                Currently, only one directory can be specified, but this definition allows for multiple in
                the future without breaking compatibility.
            output_reads_directory (str, optional): Output directory where aligned reads will be placed.
            recursive (bool, optional): Recursively find fast5 files to align in the `input_reads_directories`.

                If False, only the fast5 files directly in one of the `input_reads_directories` will be
                aligned. If True, subdirectories of those directories will also be searched recursively.
            alignment_configuration (minknow_api.analysis_configuration_pb2.AlignmentConfiguration, optional): Options to control alignment performed once basecalling reads is complete.

        Returns:
            minknow_api.basecaller_pb2.StartAlignmentResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.start_alignment,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.basecaller.Basecaller")

        unused_args = set(kwargs.keys())

        _message = StartAlignmentRequest()

        if "name" in kwargs:
            unused_args.remove("name")
            _message.name = kwargs['name']

        if "input_reads_directories" in kwargs:
            unused_args.remove("input_reads_directories")
            _message.input_reads_directories.extend(kwargs['input_reads_directories'])

        if "output_reads_directory" in kwargs:
            unused_args.remove("output_reads_directory")
            _message.output_reads_directory = kwargs['output_reads_directory']

        if "recursive" in kwargs:
            unused_args.remove("recursive")
            _message.recursive = kwargs['recursive']

        if "alignment_configuration" in kwargs:
            unused_args.remove("alignment_configuration")
            _message.alignment_configuration.CopyFrom(kwargs['alignment_configuration'])

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to start_alignment: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.start_alignment,
                              _message, _timeout,
                              [],
                              "minknow_api.basecaller.Basecaller")
    def cancel(self, _message=None, _timeout=None, **kwargs):
        """Stop a basecalling that was started by start_basecalling_reads().

        Since 3.5

        This RPC is idempotent. It may change the state of the system, but if the requested
        change has already happened, it will not fail because of this, make any additional
        changes or return a different value.

        Args:
            _message (minknow_api.basecaller_pb2.CancelRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            id (str, optional): An identifier as returned from a call to start() or list().

        Returns:
            minknow_api.basecaller_pb2.CancelResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.cancel,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.basecaller.Basecaller")

        unused_args = set(kwargs.keys())

        _message = CancelRequest()

        if "id" in kwargs:
            unused_args.remove("id")
            _message.id = kwargs['id']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to cancel: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.cancel,
                              _message, _timeout,
                              [],
                              "minknow_api.basecaller.Basecaller")
    def get_info(self, _message=None, _timeout=None, **kwargs):
        """Gets information about one or more basecalling operations.

        Since 3.5

        This RPC has no side effects. Calling it will have no effect on the state of the
        system. It is safe to call repeatedly, or to retry on failure, although there is no
        guarantee it will return the same information each time.

        Args:
            _message (minknow_api.basecaller_pb2.GetInfoRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
                Note that this is the time until the call ends, not the time between returned
                messages.
            preset (minknow_api.basecaller_pb2.SelectionPreset, optional): A pre-determined selection of runs.
            id (str, optional): An identifier, as returned by start().
            list (minknow_api.basecaller_pb2.GetInfoRequest.IdList, optional): A list of identifiers, as returned by start().

        Returns:
            iter of minknow_api.basecaller_pb2.GetInfoResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_info,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.basecaller.Basecaller")

        unused_args = set(kwargs.keys())

        # check oneof group 'selection'
        oneof_fields = set([
            "preset",
            "id",
            "list",
        ])

        if len(unused_args & oneof_fields) > 1:
            raise ArgumentError("get_info given multiple conflicting arguments: '{}'".format(", ".join(unused_args & oneof_fields)))

        _message = GetInfoRequest()

        if "preset" in kwargs:
            unused_args.remove("preset")
            _message.preset = kwargs['preset']

        if "id" in kwargs:
            unused_args.remove("id")
            _message.id = kwargs['id']

        if "list" in kwargs:
            unused_args.remove("list")
            _message.list.CopyFrom(kwargs['list'])

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_info: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_info,
                              _message, _timeout,
                              [],
                              "minknow_api.basecaller.Basecaller")
    def watch(self, _message=None, _timeout=None, **kwargs):
        """Monitors basecalls, returning messages when basecalls are started, stopped or receive
        progress updates.

        The current state of all currently-running basecalls will be returned in the initial set of
        messages. Optionally, the state of all already-finished runs can be included. Note that this
        initial state may be split among several responses.

        Note that progress updates may be rate limited to avoid affecting performance.

        Since 3.5

        This RPC has no side effects. Calling it will have no effect on the state of the
        system. It is safe to call repeatedly, or to retry on failure, although there is no
        guarantee it will return the same information each time.

        Args:
            _message (minknow_api.basecaller_pb2.WatchRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
                Note that this is the time until the call ends, not the time between returned
                messages.
            send_finished_runs (bool, optional): By default, no information will be sent about runs that were already finished when this call
                was made. Setting this to true will cause the state of already-finished runs to be returned.

        Returns:
            iter of minknow_api.basecaller_pb2.WatchResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.watch,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.basecaller.Basecaller")

        unused_args = set(kwargs.keys())

        _message = WatchRequest()

        if "send_finished_runs" in kwargs:
            unused_args.remove("send_finished_runs")
            _message.send_finished_runs = kwargs['send_finished_runs']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to watch: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.watch,
                              _message, _timeout,
                              [],
                              "minknow_api.basecaller.Basecaller")
    def make_alignment_index(self, _message=None, _timeout=None, **kwargs):
        """Build an alignment index file from an input fasta reference.

        This call blocks whilst the index is built.

        Since 4.3

        

        Args:
            _message (minknow_api.basecaller_pb2.MakeAlignmentIndexRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            input_alignment_reference (str, optional): Input fasta reference to use for building the index.
            output_alignment_index (str, optional): Output file path to write index (mmi file) to.

                Must have a ".mmi" extension, and the paths parent directory must exist.

        Returns:
            minknow_api.basecaller_pb2.MakeAlignmentIndexResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.make_alignment_index,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.basecaller.Basecaller")

        unused_args = set(kwargs.keys())

        _message = MakeAlignmentIndexRequest()

        if "input_alignment_reference" in kwargs:
            unused_args.remove("input_alignment_reference")
            _message.input_alignment_reference = kwargs['input_alignment_reference']

        if "output_alignment_index" in kwargs:
            unused_args.remove("output_alignment_index")
            _message.output_alignment_index = kwargs['output_alignment_index']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to make_alignment_index: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.make_alignment_index,
                              _message, _timeout,
                              [],
                              "minknow_api.basecaller.Basecaller")
    def list_post_processing_protocols(self, _message=None, _timeout=None, **kwargs):
        """Gives back a list that contains info about each possible post processing protocol script minknow is aware of.
        This will most likely be used to retrieve a suitable post processing protocol script that can be passed on to `start_post_processing_protocol`

        Since 4.4

        This RPC is idempotent. It may change the state of the system, but if the requested
        change has already happened, it will not fail because of this, make any additional
        changes or return a different value.

        Args:
            _message (minknow_api.basecaller_pb2.ListPostProcessingProtocolsRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.

        Returns:
            minknow_api.basecaller_pb2.ListPostProcessingProtocolsResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.list_post_processing_protocols,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.basecaller.Basecaller")

        unused_args = set(kwargs.keys())

        _message = ListPostProcessingProtocolsRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to list_post_processing_protocols: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.list_post_processing_protocols,
                              _message, _timeout,
                              [],
                              "minknow_api.basecaller.Basecaller")
    def list_settings_for_post_processing_protocol(self, _message=None, _timeout=None, **kwargs):
        """Find available display settings for an post processing protocol

        Since 4.4

        This RPC has no side effects. Calling it will have no effect on the state of the
        system. It is safe to call repeatedly, or to retry on failure, although there is no
        guarantee it will return the same information each time.

        Args:
            _message (minknow_api.basecaller_pb2.ListSettingsForPostProcessingProtocolRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            identifier (str, optional): specify the protocol with a string containing all the protocol's identifying components, eg:
                "SYSTEM:post_processing/artic"

        Returns:
            minknow_api.basecaller_pb2.ListSettingsForPostProcessingProtocolResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.list_settings_for_post_processing_protocol,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.basecaller.Basecaller")

        unused_args = set(kwargs.keys())

        _message = ListSettingsForPostProcessingProtocolRequest()

        if "identifier" in kwargs:
            unused_args.remove("identifier")
            _message.identifier = kwargs['identifier']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to list_settings_for_post_processing_protocol: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.list_settings_for_post_processing_protocol,
                              _message, _timeout,
                              [],
                              "minknow_api.basecaller.Basecaller")
    def update_post_processing_protocol_progress(self, _message=None, _timeout=None, **kwargs):
        """Set the progress of the currently executing post processing protocol (this API expects a run_id as more than one can be active).

        

        Args:
            _message (minknow_api.basecaller_pb2.UpdateProgressRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            id (str, optional): id of the protocol to update (stored in environment variable for python process)
            progress (float, optional): Progress indicator, 0-1.

        Returns:
            minknow_api.basecaller_pb2.UpdateProgressResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.update_post_processing_protocol_progress,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.basecaller.Basecaller")

        unused_args = set(kwargs.keys())

        _message = UpdateProgressRequest()

        if "id" in kwargs:
            unused_args.remove("id")
            _message.id = kwargs['id']

        if "progress" in kwargs:
            unused_args.remove("progress")
            _message.progress = kwargs['progress']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to update_post_processing_protocol_progress: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.update_post_processing_protocol_progress,
                              _message, _timeout,
                              [],
                              "minknow_api.basecaller.Basecaller")
    def send_ping(self, _message=None, _timeout=None, **kwargs):
        """Send a ping to the configured ping server (see system config for ping server url)

        The tracking_id and context_data section of the ping are filled in automatically by the basecall manager.

        The ping is queued internally for sending immediately, if the basecall manager fails to send the message it
        stores the message to send when possible.

        Since 5.0

        

        Args:
            _message (minknow_api.basecaller_pb2.SendPingRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            ping_data (str): The json data to send as a ping.

                note: if this string is not a valid json object, an error will be raised.

        Returns:
            minknow_api.basecaller_pb2.SendPingResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.send_ping,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.basecaller.Basecaller")

        unused_args = set(kwargs.keys())

        _message = SendPingRequest()

        if "ping_data" in kwargs:
            unused_args.remove("ping_data")
            _message.ping_data = kwargs['ping_data']
        else:
            raise ArgumentError("send_ping requires a 'ping_data' argument")

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to send_ping: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.send_ping,
                              _message, _timeout,
                              [],
                              "minknow_api.basecaller.Basecaller")
