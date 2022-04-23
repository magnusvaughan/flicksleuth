import {useEffect, useState} from "react"
import axios from "axios"

function App() {
  const [movies, setMovies] = useState(null)

  useEffect(() => {
    function fetchMovies() {
      axios.get("http://127.0.0.1:8000/api/movies").then(response => {
        console.log(response.data)
        setMovies(response.data)
      })
    }
    fetchMovies()
  })

  return (
    <div>
      {movies && movies.map((movie, index) => {
        <div key={index}>{movie.title}</div>
      })}
    </div>
  );
}

export default App;
