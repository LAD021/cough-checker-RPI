import config
import sound
import pic
import request

if __name__ == '__main__':
#    sound.getSound()
#    pic.getPic()
    print(request.test())
    soundData = {
                "cough" : open("./output/sound.mp3", "rb")
            }

    picData = {
                "figure" : open("./output/pic.jpg", "rb")
            }
    request.sendSound(soundData)
