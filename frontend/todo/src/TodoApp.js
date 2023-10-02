import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './styles/todo.css';

function TodoApp() {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState('');
  const [editingTodo, setEditingTodo] = useState(null);
  const [editedTodoTitle, setEditedTodoTitle] = useState('');

  useEffect(() => {
    axios.get('/api/todos/')
      .then((response) => {
        setTodos(response.data);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, []);

  const handleAddTodo = () => {
    axios.post('/api/todos/', { title: newTodo })
      .then((response) => {
        setTodos([...todos, response.data]);
        setNewTodo('');
      })
      .catch((error) => {
        console.error('Error creating todo:', error);
      });
  };

  const handleDeleteTodo = (id) => {
    axios.delete(`/api/todos/${id}/`).then(() => {
      setTodos(todos.filter((todo) => todo.id !== id));
    });
  };

  const handleEdit = (id, title) => {
    setEditingTodo(id);
    setEditedTodoTitle(title);
  };

  const handleSaveEdit = (id) => {
    axios.put(`/api/todos/${id}/`, { title: editedTodoTitle })
      .then(() => {
        const updatedTodos = todos.map((todo) =>
          todo.id === id ? { ...todo, title: editedTodoTitle } : todo
        );
        setTodos(updatedTodos);
        setEditingTodo(null);
      })
      .catch((error) => {
        console.error('Error updating todo:', error);
      });
  };

  const cancelEdit = () => {
    setEditingTodo(null);
    setEditedTodoTitle('');
  };

  return (
    <div className="container">
  <h1>To-Do App</h1>
  <div className="input-container">
    <input
      type="text"
      placeholder="New todo..."
      value={newTodo}
      onChange={(e) => setNewTodo(e.target.value)}
    />
    <button onClick={handleAddTodo}>Add</button>
  </div>
  <ul>
    {todos.map((todo) => (
      <li key={todo.id}>
        {editingTodo === todo.id ? (
          <div className="edit-form">
            <input
              type="text"
              value={editedTodoTitle}
              onChange={(e) => setEditedTodoTitle(e.target.value)}
            />
            <button className="edit" onClick={() => handleSaveEdit(todo.id)}>Save</button>
            <button className="cancel" onClick={cancelEdit}>Cancel</button>
          </div>
        ) : (
          <div>
            {todo.title}
            <button className="edit" onClick={() => handleEdit(todo.id, todo.title)}>Edit</button>
            <button onClick={() => handleDeleteTodo(todo.id)}>Delete</button>
          </div>
        )}
      </li>
    ))}
  </ul>
</div>

  );
}

export default TodoApp;
