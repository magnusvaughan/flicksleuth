import {useEffect, useState} from "react"
import axios from "axios"

function App() {
  const [movie, setMovie] = useState(null)
  const [cast, setCast] = useState([])
  const [revealedActors, setRevealedActors] = useState(1)
  const [answer, setAnswer] = useState(null)
  const [guess, setGuess] = useState("");
  const [finished, setFinished] = useState(false)

  useEffect(() => {
    function fetchMovies() {
      axios.get("http://127.0.0.1:8000/api/movies").then(response => {
        setMovie(response.data[0])
        setCast(response.data[0].actors.splice(0, revealedActors))
        setAnswer(response.data[0].title)
      })
    }
    fetchMovies()
  },[revealedActors])

  const handleSubmit = (evt) => {
    evt.preventDefault();
    if(guess === answer){
      setFinished(true)
      alert(`You won with only ${revealedActors} actors revealed`)
    } else {
      alert('Wrong!');
      setRevealedActors(revealedActors + 1);
    }
    setGuess("")
}

  return (!movie || !answer || !cast ? <p>Loading...</p>:
<div>
    <h1>Guess the movie</h1>
    {finished ? (<h3>You correctly guessed {answer} with {revealedActors} actors revealed</h3>) : (
    <h3>Clue: {answer.replace(/\S/g, "#")}</h3>
    )}
    <form onSubmit={handleSubmit}>
    <label>
      My Guess:
      <input type="text" value={guess}  onChange={e => setGuess(e.target.value)}/>
    </label>
    <input type="submit" value="Submit" />
  </form>
    <h3>Cast</h3>
    {cast.map((actor) => {
      return <p>{actor}</p>
    })}
</div>
  );
}

export default App;
