import { useCallback, useState } from "react"
import { History } from "../types"
import axios from "axios"
import secrets from "../secrets"

export default function IndexPage() {
  // input state variable
  const [sessionID, setSessionID] = useState<string>()
  const [history, setHistory] = useState<History>([])
  const [input, setInput] = useState("")

  // step function
  const step = useCallback(async () => {
    if (!input) return
    setInput("")
    if (!sessionID) {
      const response = await axios.post(`${secrets.API_ROOT}/step`, input)
      const { session_id, history } = response.data
      setHistory(history)
      setSessionID(session_id)
    } else {
      const response = await axios.post(`${secrets.API_ROOT}/step/${sessionID}`, input)
      const { history } = response.data
      setHistory(history)
    }
  }, [input])

  return (
    <div>
      <ul>
        {history
          .filter(({ role }) => role !== "system")
          .map(({ role, content }, index) => (
            <li key={index}>
              <span>[{role}] </span>
              <span>{content}</span>
            </li>
          ))}
      </ul>
      <form
        onSubmit={(e) => {
          e.preventDefault()
          step()
        }}
      >
        <input type="text" value={input} onChange={(e) => setInput(e.target.value)} />
        <button>Submit</button>
      </form>
    </div>
  )
}
