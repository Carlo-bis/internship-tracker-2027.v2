import React, { useState, useEffect } from 'react'
import Dashboard from './pages/Dashboard'
import './index.css'

function App() {
  const [jobOffers, setJobOffers] = useState([])
  const [applications, setApplications] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Load data from JSON files
    loadData()
  }, [])

  const loadData = async () => {
    try {
      const offersRes = await fetch('/data/job_offers.json')
      const appsRes = await fetch('/data/applications.json')
      
      if (offersRes.ok) {
        const offersData = await offersRes.json()
        setJobOffers(offersData.offers || [])
      }
      
      if (appsRes.ok) {
        const appsData = await appsRes.json()
        setApplications(appsData.applications || [])
      }
    } catch (error) {
      console.error('Error loading data:', error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      {loading ? (
        <div style={{ textAlign: 'center', padding: '2rem' }}>
          <p>Loading internship data...</p>
        </div>
      ) : (
        <Dashboard offers={jobOffers} applications={applications} onDataUpdate={loadData} />
      )}
    </div>
  )
}

export default App
