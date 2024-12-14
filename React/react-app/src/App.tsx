import Message from "./message";
import ListGroup from "./components/ListGroup";
import Alert from "./components/Alert";
import Button from "./components/Button";
import { useState } from "react";

function App() {

  const [stateVisibility, setStateVisibility] = useState(false);
  return <div>
    { stateVisibility && <Alert onClick={() => setStateVisibility(false)}>Hello There</Alert>}
    <Button color="primary" onClick={() => {
      setStateVisibility(true);
    }}>
      Click Me
    </Button>
    </div>
}

export default App;