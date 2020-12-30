import React, { useState } from 'react';
import TextField from '@material-ui/core/TextField';
import InputAdornment from "@material-ui/core/InputAdornment";
import IconButton from "@material-ui/core/IconButton";
import SearchIcon from "@material-ui/icons/Search";
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import './App.css'

function App() {

  const [keywords, setKeywords] = useState("Avengers");
  const [isLoading, setIsLoading] = useState(true);
  const [result, setResult] = useState([]);

  const handleOnChange = event => {
    setKeywords(event.target.value);
  }

  const handleOnClick = event => {
    setIsLoading(true);
    console.log('Search String: ', keywords);
    var request_uri = `http://localhost:3000/search?q=${keywords}`
    console.log("Request: ", request_uri)
    fetch(`http://localhost:3000/search?q=${keywords}`, {method: "GET"})
      .then(response => response.json())
      .then(data => {
        setResult(data.items);
        setIsLoading(false);
      })
      .catch(error => console.log(error));
  }

  return (
    <div className="App">
      <p>Netflix Show Search</p>
      <div className="search-box">
        <TextField
          label="Search"
          variant="outlined"
          onChange={handleOnChange}
          InputProps={{
            endAdornment: (
              <InputAdornment>
                <IconButton onClick={handleOnClick}>
                  <SearchIcon />
                </IconButton>
              </InputAdornment>
            )
          }}
        />
      </div>
      {!isLoading?
      <div className="result-area">
        <TableContainer component={Paper}>
          <Table aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell>Title</TableCell>
                <TableCell>Type</TableCell>
                <TableCell>Release Year</TableCell>
                <TableCell>Rating</TableCell>
                <TableCell>Description</TableCell>
                <TableCell>Duration</TableCell>
                <TableCell>Director</TableCell>
                <TableCell>Cast</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {result.map((row) => (
                <TableRow key={row.title}>
                  <TableCell component="th" scope="row">
                    {row.title}
                  </TableCell>
                  <TableCell align="right">{row.type}</TableCell>
                  <TableCell align="right">{row.release_year}</TableCell>
                  <TableCell align="right">{row.rating}</TableCell>
                  <TableCell align="right">{row.description}</TableCell>
                  <TableCell align="right">{row.duration}</TableCell>
                  <TableCell align="right">{row.director}</TableCell>
                  <TableCell align="right">{row.cast}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </div>
      :null}
    </div>
  );
}

export default App;
