import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:3000/api', // 根据实际后端API地址修改
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// 证书相关API
export const getCertificates = () => api.get('/certificates')
export const createCertificate = (data: any) => api.post('/certificates', data)
export const updateCertificate = (id: string, data: any) => api.put(`/certificates/${id}`, data)
export const deleteCertificate = (id: string) => api.delete(`/certificates/${id}`)

export default api