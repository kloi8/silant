import React, { createContext, useState, useContext } from "react";

const RoleContext = createContext();

export const RoleContextProvider = ({ children }) => {
  const [role, setRole] = useState(null); // определение роли

  return (
    <RoleContext.Provider value={{ role, setRole }}>
      {children}
    </RoleContext.Provider>
  );
};

export const useRole = () => useContext(RoleContext);