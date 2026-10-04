import React from 'react'
import { TrendingUp, FileText, CheckCircle } from 'lucide-react'

function Stats({ offers, applications }) {
  const stats = [
    { label: 'Total Offers', value: offers.length, icon: TrendingUp, color: '#3b82f6' },
    { label: 'Applications', value: applications.length, icon: FileText, color: '#10b981' },
    { label: 'Success Rate', value: applications.filter(a => a.status === 'offer').length, icon: CheckCircle, color: '#f59e0b' }
  ]

  return (
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1rem' }}>
      {stats.map((stat, idx) => {
        const Icon = stat.icon
        return (
          <div key={idx} className="card" style={{ display: 'flex', alignItems: 'center' }}>
            <Icon size={32} style={{ color: stat.color, marginRight: '1rem' }} />
            <div>
              <p style={{ color: '#94a3b8', fontSize: '0.875rem' }}>{stat.label}</p>
              <p style={{ fontSize: '1.875rem', fontWeight: 'bold' }}>{stat.value}</p>
            </div>
          </div>
        )
      })}
    </div>
  )
}

export default Stats
