[{"tag":"struct","ns":0,"name":"ALCdevice_struct","id":0,"location":"\/usr\/include\/AL\/alc.h:34:16","bitSize":0,"bitAlignment":0,"fields":null},{"tag":"typedef","ns":0,"name":"ALCdevice","location":"\/usr\/include\/AL\/alc.h:34:33","type":{"tag":"struct","ns":0,"name":"ALCdevice_struct","id":0,"location":"\/usr\/include\/AL\/alc.h:34:16","bitSize":0,"bitAlignment":0,"fields":null}},{"tag":"struct","ns":0,"name":"ALCcontext_struct","id":0,"location":"\/usr\/include\/AL\/alc.h:36:16","bitSize":0,"bitAlignment":0,"fields":null},{"tag":"typedef","ns":0,"name":"ALCcontext","location":"\/usr\/include\/AL\/alc.h:36:34","type":{"tag":"struct","ns":0,"name":"ALCcontext_struct","id":0,"location":"\/usr\/include\/AL\/alc.h:36:16","bitSize":0,"bitAlignment":0,"fields":null}},{"tag":"typedef","ns":0,"name":"ALCboolean","location":"\/usr\/include\/AL\/alc.h:39:14","type":{"tag":":char","bitSize":8,"bitAlignment":8}},{"tag":"typedef","ns":0,"name":"ALCchar","location":"\/usr\/include\/AL\/alc.h:42:14","type":{"tag":":char","bitSize":8,"bitAlignment":8}},{"tag":"typedef","ns":0,"name":"ALCbyte","location":"\/usr\/include\/AL\/alc.h:45:21","type":{"tag":":signed-char","bitSize":8,"bitAlignment":8}},{"tag":"typedef","ns":0,"name":"ALCubyte","location":"\/usr\/include\/AL\/alc.h:48:23","type":{"tag":":unsigned-char","bitSize":8,"bitAlignment":8}},{"tag":"typedef","ns":0,"name":"ALCshort","location":"\/usr\/include\/AL\/alc.h:51:15","type":{"tag":":short","bitSize":16,"bitAlignment":16}},{"tag":"typedef","ns":0,"name":"ALCushort","location":"\/usr\/include\/AL\/alc.h:54:24","type":{"tag":":unsigned-short","bitSize":16,"bitAlignment":16}},{"tag":"typedef","ns":0,"name":"ALCint","location":"\/usr\/include\/AL\/alc.h:57:13","type":{"tag":":int","bitSize":32,"bitAlignment":32}},{"tag":"typedef","ns":0,"name":"ALCuint","location":"\/usr\/include\/AL\/alc.h:60:22","type":{"tag":":unsigned-int","bitSize":32,"bitAlignment":32}},{"tag":"typedef","ns":0,"name":"ALCsizei","location":"\/usr\/include\/AL\/alc.h:63:13","type":{"tag":":int","bitSize":32,"bitAlignment":32}},{"tag":"typedef","ns":0,"name":"ALCenum","location":"\/usr\/include\/AL\/alc.h:66:13","type":{"tag":":int","bitSize":32,"bitAlignment":32}},{"tag":"typedef","ns":0,"name":"ALCfloat","location":"\/usr\/include\/AL\/alc.h:69:15","type":{"tag":":float","bitSize":32,"bitAlignment":32}},{"tag":"typedef","ns":0,"name":"ALCdouble","location":"\/usr\/include\/AL\/alc.h:72:16","type":{"tag":":double","bitSize":64,"bitAlignment":64}},{"tag":"typedef","ns":0,"name":"ALCvoid","location":"\/usr\/include\/AL\/alc.h:75:14","type":{"tag":":void"}},{"tag":"function","name":"alcCreateContext","ns":0,"location":"\/usr\/include\/AL\/alc.h:170:34","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"device","type":{"tag":":pointer","type":{"tag":"ALCdevice"}}},{"tag":"parameter","name":"attrlist","type":{"tag":":pointer","type":{"tag":"ALCint"}}}],"returnType":{"tag":":pointer","type":{"tag":"ALCcontext"}}},{"tag":"function","name":"alcMakeContextCurrent","ns":0,"location":"\/usr\/include\/AL\/alc.h:171:34","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"context","type":{"tag":":pointer","type":{"tag":"ALCcontext"}}}],"returnType":{"tag":"ALCboolean"}},{"tag":"function","name":"alcProcessContext","ns":0,"location":"\/usr\/include\/AL\/alc.h:172:34","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"context","type":{"tag":":pointer","type":{"tag":"ALCcontext"}}}],"returnType":{"tag":":void"}},{"tag":"function","name":"alcSuspendContext","ns":0,"location":"\/usr\/include\/AL\/alc.h:173:34","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"context","type":{"tag":":pointer","type":{"tag":"ALCcontext"}}}],"returnType":{"tag":":void"}},{"tag":"function","name":"alcDestroyContext","ns":0,"location":"\/usr\/include\/AL\/alc.h:174:34","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"context","type":{"tag":":pointer","type":{"tag":"ALCcontext"}}}],"returnType":{"tag":":void"}},{"tag":"function","name":"alcGetCurrentContext","ns":0,"location":"\/usr\/include\/AL\/alc.h:175:34","variadic":null,"inline":null,"storageClass":"none","parameters":null,"returnType":{"tag":":pointer","type":{"tag":"ALCcontext"}}},{"tag":"function","name":"alcGetContextsDevice","ns":0,"location":"\/usr\/include\/AL\/alc.h:176:34","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"context","type":{"tag":":pointer","type":{"tag":"ALCcontext"}}}],"returnType":{"tag":":pointer","type":{"tag":"ALCdevice"}}},{"tag":"function","name":"alcOpenDevice","ns":0,"location":"\/usr\/include\/AL\/alc.h:179:33","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"devicename","type":{"tag":":pointer","type":{"tag":"ALCchar"}}}],"returnType":{"tag":":pointer","type":{"tag":"ALCdevice"}}},{"tag":"function","name":"alcCloseDevice","ns":0,"location":"\/usr\/include\/AL\/alc.h:180:33","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"device","type":{"tag":":pointer","type":{"tag":"ALCdevice"}}}],"returnType":{"tag":"ALCboolean"}},{"tag":"function","name":"alcGetError","ns":0,"location":"\/usr\/include\/AL\/alc.h:188:30","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"device","type":{"tag":":pointer","type":{"tag":"ALCdevice"}}}],"returnType":{"tag":"ALCenum"}},{"tag":"function","name":"alcIsExtensionPresent","ns":0,"location":"\/usr\/include\/AL\/alc.h:196:33","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"device","type":{"tag":":pointer","type":{"tag":"ALCdevice"}}},{"tag":"parameter","name":"extname","type":{"tag":":pointer","type":{"tag":"ALCchar"}}}],"returnType":{"tag":"ALCboolean"}},{"tag":"function","name":"alcGetProcAddress","ns":0,"location":"\/usr\/include\/AL\/alc.h:197:33","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"device","type":{"tag":":pointer","type":{"tag":"ALCdevice"}}},{"tag":"parameter","name":"funcname","type":{"tag":":pointer","type":{"tag":"ALCchar"}}}],"returnType":{"tag":":pointer","type":{"tag":":void"}}},{"tag":"function","name":"alcGetEnumValue","ns":0,"location":"\/usr\/include\/AL\/alc.h:198:33","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"device","type":{"tag":":pointer","type":{"tag":"ALCdevice"}}},{"tag":"parameter","name":"enumname","type":{"tag":":pointer","type":{"tag":"ALCchar"}}}],"returnType":{"tag":"ALCenum"}},{"tag":"function","name":"alcGetString","ns":0,"location":"\/usr\/include\/AL\/alc.h:201:37","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"device","type":{"tag":":pointer","type":{"tag":"ALCdevice"}}},{"tag":"parameter","name":"param","type":{"tag":"ALCenum"}}],"returnType":{"tag":":pointer","type":{"tag":"ALCchar"}}},{"tag":"function","name":"alcGetIntegerv","ns":0,"location":"\/usr\/include\/AL\/alc.h:202:37","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"device","type":{"tag":":pointer","type":{"tag":"ALCdevice"}}},{"tag":"parameter","name":"param","type":{"tag":"ALCenum"}},{"tag":"parameter","name":"size","type":{"tag":"ALCsizei"}},{"tag":"parameter","name":"values","type":{"tag":":pointer","type":{"tag":"ALCint"}}}],"returnType":{"tag":":void"}},{"tag":"function","name":"alcCaptureOpenDevice","ns":0,"location":"\/usr\/include\/AL\/alc.h:205:33","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"devicename","type":{"tag":":pointer","type":{"tag":"ALCchar"}}},{"tag":"parameter","name":"frequency","type":{"tag":"ALCuint"}},{"tag":"parameter","name":"format","type":{"tag":"ALCenum"}},{"tag":"parameter","name":"buffersize","type":{"tag":"ALCsizei"}}],"returnType":{"tag":":pointer","type":{"tag":"ALCdevice"}}},{"tag":"function","name":"alcCaptureCloseDevice","ns":0,"location":"\/usr\/include\/AL\/alc.h:206:33","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"device","type":{"tag":":pointer","type":{"tag":"ALCdevice"}}}],"returnType":{"tag":"ALCboolean"}},{"tag":"function","name":"alcCaptureStart","ns":0,"location":"\/usr\/include\/AL\/alc.h:207:33","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"device","type":{"tag":":pointer","type":{"tag":"ALCdevice"}}}],"returnType":{"tag":":void"}},{"tag":"function","name":"alcCaptureStop","ns":0,"location":"\/usr\/include\/AL\/alc.h:208:33","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"device","type":{"tag":":pointer","type":{"tag":"ALCdevice"}}}],"returnType":{"tag":":void"}},{"tag":"function","name":"alcCaptureSamples","ns":0,"location":"\/usr\/include\/AL\/alc.h:209:33","variadic":null,"inline":null,"storageClass":"none","parameters":[{"tag":"parameter","name":"device","type":{"tag":":pointer","type":{"tag":"ALCdevice"}}},{"tag":"parameter","name":"buffer","type":{"tag":":pointer","type":{"tag":":void"}}},{"tag":"parameter","name":"samples","type":{"tag":"ALCsizei"}}],"returnType":{"tag":":void"}},{"tag":"typedef","ns":0,"name":"LPALCCREATECONTEXT","location":"\/usr\/include\/AL\/alc.h:212:39","type":{"tag":":function-pointer"}},{"tag":"typedef","ns":0,"name":"LPALCMAKECONTEXTCURRENT","location":"\/usr\/include\/AL\/alc.h:213:39","type":{"tag":":function-pointer"}},{"tag":"typedef","ns":0,"name":"LPALCPROCESSCONTEXT","location":"\/usr\/include\/AL\/alc.h:214:39","type":{"tag":":function-pointer"}},{"tag":"typedef","ns":0,"name":"LPALCSUSPENDCONTEXT","location":"\/usr\/include\/AL\/alc.h:215:39","type":{"tag":":function-pointer"}},{"tag":"typedef","ns":0,"name":"LPALCDESTROYCONTEXT","location":"\/usr\/include\/AL\/alc.h:216:39","type":{"tag":":function-pointer"}},{"tag":"typedef","ns":0,"name":"LPALCGETCURRENTCONTEXT","location":"\/usr\/include\/AL\/alc.h:217:39","type":{"tag":":function-pointer"}},{"tag":"typedef","ns":0,"name":"LPALCGETCONTEXTSDEVICE","location":"\/usr\/include\/AL\/alc.h:218:39","type":{"tag":":function-pointer"}},{"tag":"typedef","ns":0,"name":"LPALCOPENDEVICE","location":"\/usr\/include\/AL\/alc.h:219:39","type":{"tag":":function-pointer"}},{"tag":"typedef","ns":0,"name":"LPALCCLOSEDEVICE","location":"\/usr\/include\/AL\/alc.h:220:39","type":{"tag":":function-pointer"}},{"tag":"typedef","ns":0,"name":"LPALCGETERROR","location":"\/usr\/include\/AL\/alc.h:221:39","type":{"tag":":function-pointer"}},{"tag":"typedef","ns":0,"name":"LPALCISEXTENSIONPRESENT","location":"\/usr\/include\/AL\/alc.h:222:39","type":{"tag":":function-pointer"}},{"tag":"typedef","ns":0,"name":"LPALCGETPROCADDRESS","location":"\/usr\/include\/AL\/alc.h:223:39","type":{"tag":":function-pointer"}},{"tag":"typedef","ns":0,"name":"LPALCGETENUMVALUE","location":"\/usr\/include\/AL\/alc.h:224:39","type":{"tag":":function-pointer"}},{"tag":"typedef","ns":0,"name":"LPALCGETSTRING","location":"\/usr\/include\/AL\/alc.h:225:39","type":{"tag":":function-pointer"}},{"tag":"typedef","ns":0,"name":"LPALCGETINTEGERV","location":"\/usr\/include\/AL\/alc.h:226:39","type":{"tag":":function-pointer"}},{"tag":"typedef","ns":0,"name":"LPALCCAPTUREOPENDEVICE","location":"\/usr\/include\/AL\/alc.h:227:39","type":{"tag":":function-pointer"}},{"tag":"typedef","ns":0,"name":"LPALCCAPTURECLOSEDEVICE","location":"\/usr\/include\/AL\/alc.h:228:39","type":{"tag":":function-pointer"}},{"tag":"typedef","ns":0,"name":"LPALCCAPTURESTART","location":"\/usr\/include\/AL\/alc.h:229:39","type":{"tag":":function-pointer"}},{"tag":"typedef","ns":0,"name":"LPALCCAPTURESTOP","location":"\/usr\/include\/AL\/alc.h:230:39","type":{"tag":":function-pointer"}},{"tag":"typedef","ns":0,"name":"LPALCCAPTURESAMPLES","location":"\/usr\/include\/AL\/alc.h:231:39","type":{"tag":":function-pointer"}},{"tag":"const","name":"ALCAPIENTRY","ns":0,"location":"\/usr\/include\/AL\/alc.h:27:9","type":{"tag":":long","bitSize":32,"bitAlignment":32}},{"tag":"const","name":"ALC_APIENTRY","ns":0,"location":"\/usr\/include\/AL\/alc.h:19:10","type":{"tag":":long","bitSize":32,"bitAlignment":32}},{"tag":"const","name":"ALCAPI","ns":0,"location":"\/usr\/include\/AL\/alc.h:26:9","type":{"tag":":long","bitSize":32,"bitAlignment":32}},{"tag":"const","name":"ALC_VERSION_0_1","ns":0,"location":"\/usr\/include\/AL\/alc.h:31:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":1},{"tag":"const","name":"ALC_INVALID","ns":0,"location":"\/usr\/include\/AL\/alc.h:28:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":0},{"tag":"const","name":"AL_ALC_H","ns":0,"location":"\/usr\/include\/AL\/alc.h:2:9","type":{"tag":":long","bitSize":32,"bitAlignment":32}},{"tag":"const","name":"ALC_API","ns":0,"location":"\/usr\/include\/AL\/alc.h:12:11","type":{"tag":":long","bitSize":32,"bitAlignment":32}},{"tag":"const","name":"ALC_FALSE","ns":0,"location":"\/usr\/include\/AL\/alc.h:81:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":0},{"tag":"const","name":"ALC_FREQUENCY","ns":0,"location":"\/usr\/include\/AL\/alc.h:87:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":4103},{"tag":"const","name":"ALC_TRUE","ns":0,"location":"\/usr\/include\/AL\/alc.h:84:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":1},{"tag":"const","name":"ALC_SYNC","ns":0,"location":"\/usr\/include\/AL\/alc.h:93:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":4105},{"tag":"const","name":"ALC_REFRESH","ns":0,"location":"\/usr\/include\/AL\/alc.h:90:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":4104},{"tag":"const","name":"ALC_STEREO_SOURCES","ns":0,"location":"\/usr\/include\/AL\/alc.h:99:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":4113},{"tag":"const","name":"ALC_MONO_SOURCES","ns":0,"location":"\/usr\/include\/AL\/alc.h:96:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":4112},{"tag":"const","name":"ALC_INVALID_DEVICE","ns":0,"location":"\/usr\/include\/AL\/alc.h:105:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":40961},{"tag":"const","name":"ALC_NO_ERROR","ns":0,"location":"\/usr\/include\/AL\/alc.h:102:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":0},{"tag":"const","name":"ALC_INVALID_CONTEXT","ns":0,"location":"\/usr\/include\/AL\/alc.h:108:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":40962},{"tag":"const","name":"ALC_INVALID_VALUE","ns":0,"location":"\/usr\/include\/AL\/alc.h:114:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":40964},{"tag":"const","name":"ALC_OUT_OF_MEMORY","ns":0,"location":"\/usr\/include\/AL\/alc.h:117:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":40965},{"tag":"const","name":"ALC_DEFAULT_DEVICE_SPECIFIER","ns":0,"location":"\/usr\/include\/AL\/alc.h:129:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":4100},{"tag":"const","name":"ALC_ATTRIBUTES_SIZE","ns":0,"location":"\/usr\/include\/AL\/alc.h:125:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":4098},{"tag":"const","name":"ALC_MINOR_VERSION","ns":0,"location":"\/usr\/include\/AL\/alc.h:122:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":4097},{"tag":"const","name":"ALC_ALL_ATTRIBUTES","ns":0,"location":"\/usr\/include\/AL\/alc.h:126:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":4099},{"tag":"const","name":"ALC_EXT_CAPTURE","ns":0,"location":"\/usr\/include\/AL\/alc.h:142:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":1},{"tag":"const","name":"ALC_CAPTURE_DEVICE_SPECIFIER","ns":0,"location":"\/usr\/include\/AL\/alc.h:149:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":784},{"tag":"const","name":"ALC_DEFAULT_ALL_DEVICES_SPECIFIER","ns":0,"location":"\/usr\/include\/AL\/alc.h:159:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":4114},{"tag":"const","name":"ALC_EXTENSIONS","ns":0,"location":"\/usr\/include\/AL\/alc.h:138:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":4102},{"tag":"const","name":"ALC_DEVICE_SPECIFIER","ns":0,"location":"\/usr\/include\/AL\/alc.h:136:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":4101},{"tag":"const","name":"ALC_CAPTURE_DEFAULT_DEVICE_SPECIFIER","ns":0,"location":"\/usr\/include\/AL\/alc.h:151:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":785},{"tag":"const","name":"ALC_CAPTURE_SAMPLES","ns":0,"location":"\/usr\/include\/AL\/alc.h:153:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":786},{"tag":"const","name":"ALC_ENUMERATE_ALL_EXT","ns":0,"location":"\/usr\/include\/AL\/alc.h:157:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":1},{"tag":"const","name":"ALC_INVALID_ENUM","ns":0,"location":"\/usr\/include\/AL\/alc.h:111:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":40963},{"tag":"const","name":"ALC_MAJOR_VERSION","ns":0,"location":"\/usr\/include\/AL\/alc.h:121:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":4096},{"tag":"const","name":"ALC_ALL_DEVICES_SPECIFIER","ns":0,"location":"\/usr\/include\/AL\/alc.h:166:9","type":{"tag":":long","bitSize":32,"bitAlignment":32},"value":4115}]