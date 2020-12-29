import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ClientService } from '../../client.service';
import { AuthService } from '../../auth.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  form: FormGroup;
  constructor(
    private fb: FormBuilder,
    private client: ClientService,
    private route: Router,
    public atuh: AuthService
    ) { }
  hide = true;
  notification: boolean;
  ngOnInit(): void {
    if (this.atuh.isLogedIn) {
      // tslint:disable-next-line: no-unused-expression
      this.route.navigate['/'];
    }
    this.form = this.fb.group({
      id_u: ['', Validators.required],
      name: ['', Validators.required],
      last: ['', Validators.required],
      mail: ['', [Validators.email, Validators.required]],
      phone: ['', Validators.required],
      password: ['', Validators.required],
      age: ['', Validators.required],
      role:[''],
      id_m:[''],
      id_family:['']

    })
  }
register(){
  this.route.navigate(['/login'])
}
  async onSubmit(){
    // Se recupera el token
    if (this.form.valid){
      console.log(this.form);
      this.client.postRequest(
        'http://127.0.0.1:5000/signin',
        {
          id_u: this.form.value.id_u,
          name: this.form.value.name,
          last: this.form.value.last,
          mail: this.form.value.mail,
          phone: this.form.value.phone,
          password: this.form.value.password,
          age: this.form.value.age,
          role: '2',
          id_m: '1234567891',
          id_family:'3'
        },
        // Se envia el token
      ).subscribe(
        (response: any) => {
          console.log(response);
          this.form.reset();
          this.route.navigate(['/login'])
        }
      ),
      // tslint:disable-next-line: no-unused-expression
      (error) => {
        console.log(error.status);
        this.route.navigate(['/'])

      };
    }else{
      console.log('Error en la entrada de datos del formulario del cliente');
      this.notification = true;

    }

  }

}
