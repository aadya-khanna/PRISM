import { useEffect } from "react"
import { api } from "./api/client"
import "./App.css"

function App() {
  useEffect(() => {
    const testApi = async () => {
      const res = await api.get("/health")
      console.log(res.data)
    }

    testApi()
  }, [])

  return (
    <div className="p-6">
      <h1 className="text-xl font-semibold">Stock Recommender</h1>
    </div>
  )
}

export default App
