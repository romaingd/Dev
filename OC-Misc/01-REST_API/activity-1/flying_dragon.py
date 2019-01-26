from watson_developer_cloud import TextToSpeechV1
import json

text_to_speech = TextToSpeechV1(
    iam_apikey='DWBoa2REpHVgu5SOCSkO8dKC9_bHtp6Ql5wvYvcmorEv',
    url='https://gateway-lon.watsonplatform.net/text-to-speech/api'
)


# voices = text_to_speech.list_voices().get_result()
# print(json.dumps(voices, indent=2))

text = "I am a flying dragon with shiny red scales." \
       + " I like dancing with the witches and with their ravens." \
       + " Today I ate an antilope; it was crunchy around the horns" \
       + " and a little bit too fat near the thighs."

with open('flying_dragon.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            text,
            'audio/wav',
            'en-US_AllisonVoice'
        ).get_result().content)