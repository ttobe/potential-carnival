import { Injectable } from '@nestjs/common';
import { CreateRestaurantDto } from './dto/create-restaurant.dto';
import { UpdateRestaurantDto } from './dto/update-restaurant.dto';
import * as fs from 'fs';
import * as Papa from 'papaparse';
@Injectable()
export class RestaurantService {
  create(createRestaurantDto: CreateRestaurantDto) {
    return 'This action adds a new restaurant';
  }

  async findAll(): Promise<string> {
    // CSV 샘플 파일 경로 설정
    // const csvFilePath = 'static/data/restaurantDB_with_ratings_sample.csv';
    
    // CSV 파일 경로 설정
    const csvFilePath = 'static/data/restaurantDB_with_ratings.csv';

    try {
      // CSV 파일 읽기
      const csvData = fs.readFileSync(csvFilePath, 'utf8');

      // CSV 파싱 (Promise를 반환하는 패턴 사용)
      const parsedData = await new Promise<Papa.ParseResult>((resolve, reject) => {
        Papa.parse(csvData, {
          header: true,
          dynamicTyping: true,
          complete: resolve,
          error: reject,
        });
      });

      // JSON으로 변환
      const jsonData = JSON.stringify(parsedData.data, null, 2);


      return jsonData;
    } catch (error) {
      console.error('에러 발생:', error.message);
      throw error; // 오류가 발생하면 호출자에게 전파
    }
  }

  findOne(id: number) {
    return `This action returns a #${id} restaurant`;
  }

  update(id: number, updateRestaurantDto: UpdateRestaurantDto) {
    return `This action updates a #${id} restaurant`;
  }

  remove(id: number) {
    return `This action removes a #${id} restaurant`;
  }
}
