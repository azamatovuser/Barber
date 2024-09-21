from aiogram import Bot, Dispatcher, filters, types, F
import asyncio
from config import TOKEN
from database import Database
from buttons.reply_buttons import add_button
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
db = Database()


class AddProduct(StatesGroup):
    name = State()
    price = State()
    image = State()


@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
    db.create_table_product()
    await message.answer("Yo what's up nigga?",
                         reply_markup=add_button)


@dp.message(F.text == "Добавить товар 🦍")
async def add_function(message: types.Message, state: FSMContext):
    await state.set_state(AddProduct.name)
    await message.answer("Введите название товара")


@dp.message(F.text == "Посмотреть все товары")
async def add_function(message: types.Message):
    data = db.get_products()
    await message.answer(f"{data}")


@dp.message(AddProduct.name)
async def name_function(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(AddProduct.price)
    await message.answer("Введите цену товара")


@dp.message(AddProduct.price)
async def name_function(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await state.set_state(AddProduct.image)
    await message.answer("Отправьте картинку товара")


@dp.message(AddProduct.image)
async def name_function(message: types.Message, state: FSMContext):
    image = message.photo[0].file_id
    await state.update_data(image=image)

    data = await state.get_data()

    db.add_product(data['name'], data['price'], data['image'])

    await message.answer("Вы успешно отправили товар")
    await state.clear()




async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
