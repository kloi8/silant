import React, { useState } from 'react';
import MyButton from '../UI/Button/MyButton';
import ListService from '../Services/listServise';

const AddListsObjects = ({ url, label, onAddSuccess  }) => {
    const [isOpen, setIsOpen] = useState(false);
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [error, setError] = useState('');

    const handleSubmit = async () => {
        if (!title) {
            setError('Название обязательно');
            return;
        }
        
        try {
            await ListService.addObject(url, { title, description });
            setIsOpen(false);
            setTitle('');
            setDescription('');
            setError('');
            if (onAddSuccess) onAddSuccess();  // Обновление списка, если передана такая функция
        } catch (error) {
            console.error(error);
            setError('Произошла ошибка при добавлении объекта');
        }
    };

    return (
        <div>
            <MyButton onClick={() => setIsOpen(true)}>{label}</MyButton>
            {isOpen && (
                <div>
                    <input
                        type="text"
                        placeholder="Название"
                        value={title}
                        onChange={(e) => setTitle(e.target.value)}
                    />
                    <input
                        type="text"
                        placeholder="Описание"
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                    />
                    {error && <p>{error}</p>}
                    <MyButton onClick={handleSubmit}>Добавить</MyButton>
                    <MyButton onClick={() => setIsOpen(false)}>Отмена</MyButton>
                </div>
            )}
        </div>
    );
};

export default AddListsObjects;