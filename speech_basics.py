import wave


obj  = wave.open("/home/saad-alam/Documents/Ibex_workspace/audio_processing_with_python/blues.00000.wav", "rb")

print("get number of channels : ", obj.getnchannels())
print("get width of sample : ", obj.getsampwidth())
print("get sample rate : ", obj.getframerate())
print("get number of frames : ", obj.getnframes())
print("get number of parameters : ", obj.getparams())

time_of_wav_file = obj.getnframes()/obj.getframerate()

print("get time for audio wave file : ", time_of_wav_file)

# read frame by using wav module

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames) / 2)

obj.close()

# writing wave file using wave module
obj_new = wave.open("/home/saad-alam/Documents/Ibex_workspace/audio_processing_with_python/blues.000001.wav", "wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(22050)
obj_new.writeframes(frames)
obj_new.close()