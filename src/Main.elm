import Browser
import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)
import Http
import Json.Decode exposing (Decoder, field, list, string)
import Url.Builder exposing (absolute)

main =
  Browser.element
    { init = init
    , update = update
    , subscriptions = subscriptions
    , view = view
    }

type alias Model =
  { sentences: List String
  }

init : () -> (Model, Cmd Msg)
init _ =
  ( Model  []
  , Cmd.none
  )

type Msg
  = FetchData | StoreData (Result Http.Error (List String))

update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
  case msg of
    FetchData ->
      ( model
      , fetchData
      )

    StoreData (Ok data) ->
      ( { model | sentences = data }
      , Cmd.none
      )

    StoreData (Err _) ->
      ( { model | sentences = ["Janky Danky"] }
      , Cmd.none
      )


subscriptions : Model -> Sub Msg
subscriptions model =
  Sub.none

view : Model -> Html Msg
view model =
  div []
    [ h2 [] [ text "Wittgen" ]
    , button [ onClick FetchData ] [ text "Fetch Data!" ]
    , div [] (List.map displaySentence model.sentences)
    ]

displaySentence : String -> Html Msg
displaySentence sentence =
  div [] [ text sentence ]

fetchData : Cmd Msg
fetchData =
  Http.send StoreData getBook

getBook : Http.Request (List String)
getBook =
  Http.get (absolute [ "api", "book", "1" ] []) sentencesDecoder

sentencesDecoder : Decoder (List String)
sentencesDecoder =
  field "sentences" (list string)
