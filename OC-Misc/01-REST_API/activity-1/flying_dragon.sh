curl -u "apikey:DWBoa2REpHVgu5SOCSkO8dKC9_bHtp6Ql5wvYvcmorEv" -X POST \
--header "Content-Type: application/json" \
--header "Accept: audio/wav" \
--data '{"text": "I am a flying dragon with shiny red scales. \
I like dancing with the witches and with their ravens. \
Today I ate an antilope; it was crunchy around the horns \
and a little bit too fat near the thighs."}' \
--output flying_dragon.wav \
"https://gateway-lon.watsonplatform.net/text-to-speech/api/v1/synthesize"