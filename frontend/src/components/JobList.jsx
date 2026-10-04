import React from 'react'
import JobCard from './JobCard'

function JobList({ offers, applications, onUpdate }) {
  if (offers.length === 0) {
    return (
      <div className="card" style={{ textAlign: 'center', padding: '3rem' }}>
        <p style={{ color: '#94a3b8' }}>No opportunities found matching your criteria.</p>
      </div>
    )
  }

  return (
    <div style={{ display: 'grid', gap: '1.5rem' }}>
      {offers.map(offer => (
        <JobCard 
          key={offer.id} 
          offer={offer} 
          isApplied={applications.some(app => app.offerId === offer.id)}
          onUpdate={onUpdate}
        />
      ))}
    </div>
  )
}

export default JobList
