import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Table.css';

const Table = ({ data, columns, onRowClick }) => {
  const [sortConfig, setSortConfig] = useState({ key: null, direction: 'asc' });
  const navigate = useNavigate();

  const handleSort = (key) => {
    const direction = sortConfig.key === key && sortConfig.direction === 'asc' ? 'desc' : 'asc';
    setSortConfig({ key, direction });
  };

  const sortedData = [...data].sort((a, b) => {
    if (!sortConfig.key) return 0;
    const order = sortConfig.direction === 'asc' ? 1 : -1;
    return a[sortConfig.key] > b[sortConfig.key] ? order : -order;
  });

  const handleRowClick = (row) => {
    if (onRowClick) {
      onRowClick(row);
    } else {
      navigate(`/${columns[0].key}/${row[columns[0].key]}`);
    }
  };

  return (
    <table className="table">
      <thead>
        <tr>
          {columns.map((col) => (
            <th key={col.key} onClick={() => handleSort(col.key)}>
              {col.label}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {sortedData.map((row, index) => (
          <tr key={index} onClick={() => handleRowClick(row)}>
            {columns.map((col) => (
              <td key={col.key}>{row[col.key]}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default Table;