import React from 'react'
import { ExternalLink, CheckCircle, FileText } from 'lucide-react'

function JobCard({ offer, isApplied, onUpdate }) {
  const handleApply = () => {
    alert(`Application to ${offer.company} - ${offer.title} registered!\n\nDownload your personalized CV and cover letter from the download button.`)
    onUpdate()
  }

  const getStatusBadge = () => {
    if (isApplied) return <span className="badge applied">Applied</span>
    return <span className="badge new">New</span>
  }

  return (
    <div className="card">
      <div style={{ marginBottom: '1rem' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '0.5rem' }}>
          <div>
            <h3 style={{ fontSize: '1.125rem', fontWeight: 'bold', marginBottom: '0.25rem' }}>
              {offer.title}
            </h3>
            <p style={{ color: '#94a3b8', fontSize: '0.875rem' }}>
              {offer.company} • {offer.location}
            </p>
          </div>
          {getStatusBadge()}
        </div>
      </div>

      <p style={{ color: '#cbd5e1', fontSize: '0.875rem', marginBottom: '1rem', lineHeight: '1.5' }}>
        {offer.description?.substring(0, 200)}...
      </p>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.75rem', marginBottom: '1rem', fontSize: '0.75rem', color: '#94a3b8' }}>
        <div>📅 Posted: {new Date(offer.posted_date).toLocaleDateString()}</div>
        <div>⏰ Deadline: {offer.deadline}</div>
        <div>🎯 Steps: {offer.application_steps}</div>
        <div>📍 Country: {offer.country}</div>
      </div>

      <div style={{ display: 'flex', gap: '0.75rem' }}>
        <button onClick={handleApply} style={{ flex: 1 }}>
          <CheckCircle size={16} style={{ marginRight: '0.5rem', display: 'inline' }} />
          Mark Applied
        </button>
        <button 
          onClick={() => window.open(offer.link, '_blank')}
          style={{ flex: 1, background: '#64748b' }}
        >
          <ExternalLink size={16} style={{ marginRight: '0.5rem', display: 'inline' }} />
          View
        </button>
        <button 
          onClick={() => alert('Download personalized CV and cover letter for this position')}
          style={{ flex: 1, background: '#10b981' }}
        >
          <FileText size={16} style={{ marginRight: '0.5rem', display: 'inline' }} />
          Download
        </button>
      </div>
    </div>
  )
}

export default JobCard
