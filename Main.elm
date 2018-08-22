import Html exposing (Html, div, text)

main =
  Html.beginnerProgram { model = {}, view = view, update = update }

update msg model = model

view model =
  div [] [
    text "Hello from Wittgen!"
  ]
