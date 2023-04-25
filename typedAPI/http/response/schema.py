
import typing


EllipsisType = type(...)

Status = int

Headers = dict

Body = str | dict | bytes

Response = Status | typing.Tuple[Status, Headers] | typing.Tuple[Status, Headers, Body]

NormalisedResponse = typing.Tuple[Status, Headers | EllipsisType | None, Body | EllipsisType | None]




HttpContentType = typing.Literal[
    'application/atom+xml',
    'application/ecmascript',
    'application/EDI-X12',
    'application/EDIFACT',
    'application/json',
    'application/javascript',
    'application/octet-stream',
    'application/ogg',
    'application/pdf',
    'application/postscript',
    'application/rdf+xml',
    'application/rss+xml',
    'application/soap+xml',
    'application/font-woff',
    'application/xhtml+xml',
    'application/xml',
    'application/xml-dtd',
    'application/xop+xml',
    'application/zip',
    'application/gzip',
    'audio/basic',
    'audio/L24',
    'audio/mp4',
    'audio/mpeg',
    'audio/ogg',
    'audio/vorbis',
    'audio/vnd.rn-realaudio',
    'audio/vnd.wave',
    'audio/webm',
    'image/gif',
    'image/jpeg',
    'image/pjpeg',
    'image/png',
    'image/svg+xml',
    'image/tiff',
    'image/vnd.microsoft.icon',
    'image/vnd.wap.wbmp',
    'image/webp',
    'multipart/mixed',
    'multipart/alternative',
    'multipart/related',
    'multipart/form-data',
    'text/css',
    'text/csv',
    'text/html',
    'text/javascript',
    'text/plain',
    'text/xml',
    'video/3gpp',
    'video/3gpp2',
    'video/h261',
    'video/h263',
    'video/h264',
    'video/jpeg',
    'video/jpm',
    'video/mj2',
    'video/mp4',
    'video/mpeg',
    'video/ogg',
    'video/quicktime',
    'video/vnd.dece.hd',
    'video/vnd.dece.mobile',
    'video/vnd.dece.pd',
    'video/vnd.dece.sd',
    'video/vnd.dece.video',
    'video/vnd.fvt',
    'video/vnd.mpegurl',
    'video/vnd.ms-playready.media.pyv',
    'video/vnd.uvvu.mp4',
    'video/vnd.vivo',
    'video/webm',
    'video/x-f4v',
    'video/x-fli',
    'video/x-flv',
    'video/x-m4v',
    'video/x-matroska',
    'video/x-mng',
    'video/x-ms-asf',
    'video/x-ms-vob',
    'video/x-ms-wm',
    'video/x-ms-wmv',
    'video/x-ms-wmx',
    'video/x-ms-wvx',
    'video/x-msvideo',
    'video/x-sgi-movie',
]


