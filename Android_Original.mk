LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

$(call import-add-path,$(LOCAL_PATH)/../../../cocos2d)
$(call import-add-path,$(LOCAL_PATH)/../../../cocos2d/external)
$(call import-add-path,$(LOCAL_PATH)/../../../cocos2d/cocos)
$(call import-add-path,$(LOCAL_PATH)/../../../cocos2d/cocos/audio/include)

LOCAL_MODULE := __UPDATE_CMAKE_GAME_NAME_LOCAL_MODULE__

LOCAL_MODULE_FILENAME := __UPDATE_CMAKE_GAME_NAME_LOCAL_MODULE_FILENAME__

LOCAL_SRC_FILES := hellocpp/main.cpp \
                  __UPDATE_CMAKE_GAME_SOURCES__

LOCAL_CFLAGS := -std=c++11
LOCAL_C_INCLUDES := $(LOCAL_PATH)/../../../Classes \
                    __UPDATE_CMAKE_INCLUDE_DIRECTORIES__

# _COCOS_HEADER_ANDROID_BEGIN
# _COCOS_HEADER_ANDROID_END


LOCAL_STATIC_LIBRARIES := cocos2dx_static

# _COCOS_LIB_ANDROID_BEGIN
# _COCOS_LIB_ANDROID_END

include $(BUILD_SHARED_LIBRARY)

$(call import-module,.)

# _COCOS_LIB_IMPORT_ANDROID_BEGIN
# _COCOS_LIB_IMPORT_ANDROID_END
