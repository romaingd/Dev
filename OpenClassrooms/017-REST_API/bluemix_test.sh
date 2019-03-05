curl -u "apikey:8w50uefnFq9myaxq9HK9y9_DMqaA_YpVb0QgwthZpMTc" -X POST \
--header "Content-Type: audio/flac" \
--header "Transfer-Encoding: chunked" \
--data-binary @"./audio-file.flac" \
"https://gateway-lon.watsonplatform.net/speech-to-text/api/v1/recognize?continuous=true"