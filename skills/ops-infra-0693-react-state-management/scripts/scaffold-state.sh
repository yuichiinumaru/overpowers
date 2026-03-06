#!/bin/bash

# Helper script to scaffold React state management boilerplate
# Usage: ./scaffold-state.sh <type> <name>
# Types: zustand, redux, jotai

TYPE=$1
NAME=$2

if [[ -z "$TYPE" || -z "$NAME" ]]; then
  echo "Usage: $0 <type> <name>"
  echo "Types: zustand, redux, jotai"
  exit 1
fi

case $TYPE in
  zustand)
    cat <<EOF > "use${NAME^}Store.ts"
import { create } from 'zustand'
import { devtools, persist } from 'zustand/middleware'

interface ${NAME^}State {
  data: any | null
  setData: (data: any) => void
  reset: () => void
}

export const use${NAME^}Store = create<${NAME^}State>()(
  devtools(
    persist(
      (set) => ({
        data: null,
        setData: (data) => set({ data }),
        reset: () => set({ data: null }),
      }),
      { name: '${NAME}-storage' }
    )
  )
)
EOF
    echo "Scaffolded Zustand store: use${NAME^}Store.ts"
    ;;
  redux)
    cat <<EOF > "${NAME}Slice.ts"
import { createSlice, PayloadAction } from '@reduxjs/toolkit'

interface ${NAME^}State {
  data: any | null
  status: 'idle' | 'loading' | 'succeeded' | 'failed'
}

const initialState: ${NAME^}State = {
  data: null,
  status: 'idle',
}

const ${NAME}Slice = createSlice({
  name: '${NAME}',
  initialState,
  reducers: {
    setData: (state, action: PayloadAction<any>) => {
      state.data = action.payload
    },
    reset: (state) => {
      state.data = null
      state.status = 'idle'
    },
  },
})

export const { setData, reset } = ${NAME}Slice.actions
export default ${NAME}Slice.reducer
EOF
    echo "Scaffolded Redux slice: ${NAME}Slice.ts"
    ;;
  jotai)
    cat <<EOF > "${NAME}Atoms.ts"
import { atom } from 'jotai'

export const ${NAME}Atom = atom<any | null>(null)
export const ${NAME}StatusAtom = atom<'idle' | 'loading' | 'succeeded' | 'failed'>('idle')

export const reset${NAME^}Atom = atom(null, (get, set) => {
  set(${NAME}Atom, null)
  set(${NAME}StatusAtom, 'idle')
})
EOF
    echo "Scaffolded Jotai atoms: ${NAME}Atoms.ts"
    ;;
  *)
    echo "Invalid type: $TYPE. Use zustand, redux, or jotai."
    exit 1
    ;;
esac
