/**
 * Reusable Interaction Design Component Templates (React + Framer Motion).
 */

/*
import { motion, AnimatePresence } from "framer-motion";
import { useState } from "react";

// 1. Interactive Button with Spring Physics
export function InteractiveButton({ children, onClick, className = "" }) {
  return (
    <motion.button
      onClick={onClick}
      whileHover={{ scale: 1.02 }}
      whileTap={{ scale: 0.98 }}
      transition={{ type: "spring", stiffness: 400, damping: 17 }}
      className={`px-4 py-2 bg-blue-600 text-white rounded-lg ${className}`}
    >
      {children}
    </motion.button>
  );
}

// 2. Skeleton Screen for Loading States
export function CardSkeleton() {
  return (
    <div className="animate-pulse p-4 border rounded-lg">
      <div className="h-48 bg-gray-200 rounded-lg mb-4" />
      <div className="h-4 bg-gray-200 rounded w-3/4 mb-2" />
      <div className="h-4 bg-gray-200 rounded w-1/2" />
    </div>
  );
}

// 3. Smooth Toggle Switch
export function Toggle({ checked, onChange }) {
  return (
    <button
      role="switch"
      aria-checked={checked}
      onClick={() => onChange(!checked)}
      className={`
        relative w-12 h-6 rounded-full transition-colors duration-200
        ${checked ? "bg-blue-600" : "bg-gray-300"}
      `}
    >
      <motion.span
        className="absolute top-1 left-1 w-4 h-4 bg-white rounded-full shadow"
        animate={{ x: checked ? 24 : 0 }}
        transition={{ type: "spring", stiffness: 500, damping: 30 }}
      />
    </button>
  );
}

// 4. Page Transition Wrapper
export function PageTransition({ children, mode = "wait" }) {
  return (
    <AnimatePresence mode={mode}>
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: -20 }}
        transition={{ duration: 0.3 }}
      >
        {children}
      </motion.div>
    </AnimatePresence>
  );
}
*/
