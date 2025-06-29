import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [files, setFiles] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    // Read API base URL from environment variable
    const apiBase = import.meta.env.VITE_API_GATEWAY_URL
    const apiUrl = apiBase + '/list'
    fetch(apiUrl)
      .then(res => {
        if (!res.ok) throw new Error('Failed to fetch audio list')
        return res.json()
      })
      .then(setFiles)
      .catch(err => setError(err.message))
      .finally(() => setLoading(false))
  }, [])

  return (
    <div className="audio-list-container">
      <h1>News Audio Files</h1>
      {loading && <p>Loading...</p>}
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
      {!loading && !error && files.length === 0 && <p>No audio files found.</p>}
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {files.map(file => (
          <li key={file.key} style={{ marginBottom: '1.5em' }}>
            <audio controls src={file.url} style={{ width: '100%' }} />
            <div style={{ fontSize: '0.9em', color: '#555' }}>{file.key}</div>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App
