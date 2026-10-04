import React, { useState } from 'react'

function Filters({ onFilter, offers }) {
  const [filters, setFilters] = useState({
    company: '',
    location: '',
    category: ''
  })

  const locations = [...new Set(offers.map(o => o.location))]
  const categories = [...new Set(offers.map(o => o.category))]

  const handleChange = (e) => {
    const { name, value } = e.target
    const newFilters = { ...filters, [name]: value }
    setFilters(newFilters)
    onFilter(newFilters)
  }

  return (
    <div className="card">
      <h3 style={{ fontSize: '1.125rem', fontWeight: 'bold', marginBottom: '1rem' }}>
        🔍 Filters
      </h3>

      <div style={{ display: 'grid', gap: '1rem' }}>
        <div>
          <label style={{ display: 'block', fontSize: '0.75rem', textTransform: 'uppercase', marginBottom: '0.5rem', color: '#94a3b8' }}>
            Company
          </label>
          <input
            type="text"
            name="company"
            placeholder="Search company..."
            value={filters.company}
            onChange={handleChange}
            style={{ width: '100%' }}
          />
        </div>

        <div>
          <label style={{ display: 'block', fontSize: '0.75rem', textTransform: 'uppercase', marginBottom: '0.5rem', color: '#94a3b8' }}>
            Location
          </label>
          <select name="location" value={filters.location} onChange={handleChange} style={{ width: '100%' }}>
            <option value="">All Locations</option>
            {locations.map(loc => (
              <option key={loc} value={loc}>{loc}</option>
            ))}
          </select>
        </div>

        <div>
          <label style={{ display: 'block', fontSize: '0.75rem', textTransform: 'uppercase', marginBottom: '0.5rem', color: '#94a3b8' }}>
            Category
          </label>
          <select name="category" value={filters.category} onChange={handleChange} style={{ width: '100%' }}>
            <option value="">All Categories</option>
            {categories.map(cat => (
              <option key={cat} value={cat}>{cat.replace('_', ' ')}</option>
            ))}
          </select>
        </div>
      </div>
    </div>
  )
}

export default Filters
