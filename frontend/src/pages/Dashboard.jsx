import React, { useState } from 'react'
import JobList from '../components/JobList'
import Filters from '../components/Filters'
import Stats from '../components/Stats'
import { Menu, X } from 'lucide-react'

function Dashboard({ offers, applications, onDataUpdate }) {
  const [filteredOffers, setFilteredOffers] = useState(offers)
  const [showFilters, setShowFilters] = useState(true)
  const [filters, setFilters] = useState({
    company: '',
    location: '',
    category: '',
    status: 'all'
  })

  const applyFilters = (newFilters) => {
    setFilters(newFilters)
    
    let filtered = offers.filter(offer => {
      if (newFilters.company && !offer.company.toLowerCase().includes(newFilters.company.toLowerCase())) return false
      if (newFilters.location && offer.location !== newFilters.location) return false
      if (newFilters.category && offer.category !== newFilters.category) return false
      return true
    })
    
    setFilteredOffers(filtered)
  }

  return (
    <div style={{ minHeight: '100vh', backgroundColor: '#0f172a' }}>
      {/* Header */}
      <header style={{
        backgroundColor: '#1e293b',
        borderBottom: '1px solid rgba(100, 116, 139, 0.3)',
        padding: '1.5rem',
        marginBottom: '2rem'
      }}>
        <div style={{ maxWidth: '1400px', margin: '0 auto', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div>
            <h1 style={{ fontSize: '1.875rem', fontWeight: 'bold', marginBottom: '0.5rem' }}>
              🚀 Internship Tracker 2027
            </h1>
            <p style={{ color: '#94a3b8' }}>Summer internship automation for Carlo Bisaglia</p>
          </div>
          <button onClick={() => setShowFilters(!showFilters)} style={{ background: 'transparent', color: 'white' }}>
            {showFilters ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>
      </header>

      <div style={{ maxWidth: '1400px', margin: '0 auto', padding: '0 1rem' }}>
        {/* Stats */}
        <Stats offers={offers} applications={applications} />

        <div style={{ display: 'grid', gridTemplateColumns: showFilters ? '300px 1fr' : '1fr', gap: '2rem', marginTop: '2rem' }}>
          {/* Filters Sidebar */}
          {showFilters && (
            <div>
              <Filters onFilter={applyFilters} offers={offers} />
            </div>
          )}

          {/* Job List */}
          <div>
            <h2 style={{ fontSize: '1.5rem', marginBottom: '1rem' }}>
              Available Opportunities ({filteredOffers.length})
            </h2>
            <JobList offers={filteredOffers} applications={applications} onUpdate={onDataUpdate} />
          </div>
        </div>
      </div>

      {/* Footer */}
      <footer style={{
        marginTop: '4rem',
        paddingTop: '2rem',
        paddingBottom: '2rem',
        borderTop: '1px solid rgba(100, 116, 139, 0.3)',
        color: '#94a3b8',
        textAlign: 'center'
      }}>
        <p>Last updated: {new Date().toLocaleString()}</p>
        <p style={{ fontSize: '0.875rem', marginTop: '0.5rem' }}>
          Internship tracker built with React + GitHub Actions automation
        </p>
      </footer>
    </div>
  )
}

export default Dashboard
