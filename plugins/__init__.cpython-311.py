�
    ��cc�  �                   �  � d dl mZ d dl mZ d dlmZmZmZ d dlm	Z	m
Z
mZ d dlmZ d dlZd dlZ ej         ej        dg�  �        ej         z  �  �        ded	efd
��   �         Z ej         ej        dg�  �        ej         z  �  �        d� �   �         Z ej         ej        dg�  �        ej         z  �  �        ded	efd��   �         ZdS )�    )�filters)�Client)�InlineKeyboardButton�InlineKeyboardMarkup�Message)�LOGGER�prefixes�
AUTH_USERS)�ConfigN�start�bot�mc              �   �Z   K  � | �                     |j        j        dd��  �        � d {V �� d S )Nz1https://telegra.ph/file/cef3ef6ee69126c23bfe3.jpgu[  **Hi i am All in One Extractor Bot**.
Press **/pw** for **Physics Wallah**..

Press **/e1** for **E1 Coaching App**..

Press **/vidya** for **Vidya Bihar App**..

Press **/ocean** for **Ocean Gurukul App**..

Press **/winners** for **The Winners Institute**..

Press **/rgvikramjeet** for **Rgvikramjeet App**..

Press **/txt** for  **Ankit With Rojgar,**
**The Mission Institute,**
**The Last Exam App**..

Press **/cp** for **classplus appp**..

Press **/cw** for **careerwill app**..

Press **/khan** for **Khan Gs app**..

Press **/exampur** for ** Exampur app**..

Press **/samyak** for ** Samayak Ias**..

Press **/mgconcept** for **Mgconcept app**..

Press **/down** for **For Downloading Url lists**..

Press **/forward** To **Forward from One channel to others**..

**𝗕𝗼𝘁 𝗢𝘄𝗻𝗲𝗿 : 𝒞𝓇𝓎𝓅𝓉💞𝓈𝓉𝒶𝓇𝓀**)�photo�caption)�
send_photo�chat�id�r   r   s     �;/storage/emulated/0/Download/All_In_One/plugins/__init__.py�	Start_msgr   
   sd   � � � �
�.�.��F�I�
=�s� � t� t� t� t� t� t� t� t� t� t� t�    �restartc              �   �   K  � |�                     dd�  �        � d {V �� t          j        t          j        t          j        gt          j        �R �  d S )Nz
Restarted!T)�
reply_text�os�execl�sys�
executable�argv)�_r   s     r   �restart_handlerr"   #   sR   � � � �
�,�,�|�T�
*�
*�*�*�*�*�*�*�*��H�S�^�S�^�7�c�h�7�7�7�7�7�7r   �logc              �   �V   K  � | �                     |j        j        d�  �        � d {V �� d S )Nzlog.txt)�send_documentr   r   r   s     r   �log_msgr&   (   s8   � � � �
�
�
�A�F�I�y�
1�
1�1�1�1�1�1�1�1�1�1r   )�pyrogramr   r   �stark�pyrogram.typesr   r   r   �mainr   r	   r
   �configr   r   r   �
on_message�command�editedr   r"   r&   � r   r   �<module>r0      s�  �� � � � � � � $� $� $� $� $� $� N� N� N� N� N� N� N� N� N� N� -� -� -� -� -� -� -� -� -� -� � � � � � � 	�	�	�	� 
�
�
�
� ���/�'�/�7�)�,�,����>�?�?�t�� t�G� t� t� t� @�?�t�0 ���/�'�/�9�+�.�.�'�.��@�A�A�8� 8� B�A�8� ���/�'�/�5�'�*�*�g�n�_�<�=�=�2�u� 2�'� 2� 2� 2� >�=�2� 2� 2r   